from collections import defaultdict

from feature_extractor import extract_features
from window_aggregator import add_to_window, aggregate_window, feature_window
from anomaly_model import train_model, predict_anomaly


def read_log_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()


def parse_logs(logs):
    events = []

    for line in logs:
        parts = line.strip().split(" ", 3)
        if len(parts) < 4:
            continue

        timestamp = parts[0] + " " + parts[1]
        level = parts[2]
        message = parts[3]

        events.append({
            "timestamp": timestamp,
            "level": level,
            "message": message
        })

    return events


def detect_rule_based(events):
    report = defaultdict(int)

    for event in events:
        if event["level"] == "ERROR":
            report["error_count"] += 1
        elif event["level"] == "WARN":
            report["warn_count"] += 1

        if "Packet Loss" in event["message"]:
            report["packet_loss_count"] += 1

        if "Timeout" in event["message"]:
            report["timeout_count"] += 1

    return report


def main():
    log_file_path = "../data/raw_logs/sample_modem.log"

    logs = read_log_file(log_file_path)
    events = parse_logs(logs)

    # Rule-based detection
    rule_features = detect_rule_based(events)
    print("\n--- Rule-based Detection ---")
    print(rule_features)

    # Feature extraction
    features = extract_features(events)
    add_to_window(features)

    # ML detection once window is filled
    if len(feature_window) >= 3:
        aggregated_features = aggregate_window()
        model = train_model(list(feature_window))
        is_anomaly = predict_anomaly(model, aggregated_features)

        print("\n--- ML Windowed Detection ---")
        if is_anomaly:
            print("🚨 Anomalous Behavior Detected Over Time")
        else:
            print("✅ Behavior Normal")


if __name__ == "__main__":
    main()
