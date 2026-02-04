def read_log_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines


def analyze_logs(logs):
    total_lines = len(logs)
    errors = [line for line in logs if "ERROR" in line]
    warnings = [line for line in logs if "WARN" in line]

    print("Total log entries:", total_lines)
    print("Warnings:", len(warnings))
    print("Errors:", len(errors))


if __name__ == "__main__":
    log_file_path = "../data/raw_logs/sample_modem.log"
    logs = read_log_file(log_file_path)
    analyze_logs(logs)
