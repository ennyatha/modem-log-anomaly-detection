from collections import defaultdict
from feature_extractor import extract_features


def read_log_file(file_path):
    with open(file_path, 'r') as file:
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
    print("\n--- Anomaly Report ---")
    for key, value in report.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    log_file_path = "../data/raw_logs/sample_modem.log"
    logs = read_log_file(log_file_path)
    events = parse_logs(logs)
    report = detect_anomalies(events)
    print_report(report)
    features = extract_features(events)

    print("\n--- Extracted Features ---")
    for key, value in features.items():
        print(f"{key}: {value}")

