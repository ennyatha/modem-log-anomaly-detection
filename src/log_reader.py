from collections import defaultdict
from feature_extractor import extract_features
from anomaly_model import train_model, predict_anomaly
from window_aggregator import add_to_window, aggregate_window


def read_log_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()


def parse_logs(logs):
    events = []
    for line in logs:
        parts = line.strip().split(" ", 3)
        if len(parts) < 4:
            continue

        events.append({
            "timestamp": parts[0] + " " + parts[1],
            "level": parts[2],
            "message": parts[3]
        })
    return events


def detect_anomalies(events):
    anomaly_report = defaultdict(int)

    for event in events:
        if event["level"] == "ERROR":
            anomaly_report["ERROR"] += 1
        elif event["level"] == "WARN":
            anomaly_report["WARN"] += 1

        if "Packet Loss" in event["message"]:
            anomaly_report["PACKET_LOSS"] += 1

        if "Timeout" in event["message"]:
            anomaly_report["TIMEOUT"] += 1

    return anomaly_report


def print_report(report):
    print("\n--- Rule-Based Anomaly Report ---")
    for key, value in report.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    log_file_path = "../data/raw_logs/sample_modem.log"

    logs = read_log_file(log_file_path)
    events = parse_logs(logs)

    # Rule-based detection
    report = detect_anomalies(events)
    print_report(report)

    # Feature extraction
    features = extract_features(events)

    # Window-based ML detection
    add_to_window(features)

    if len(features) > 0:
        window_features = aggregate_window()
        model = train_model(window_features)
        is_anomaly = predict_anomaly(model, window_features)

        print("\n--- ML Windowed Detection ---")
        if is_anomaly:
            print("🚨 Anomalous Behavior Detected Over Time")
        else:
            print("✅ Behavior Normal")
