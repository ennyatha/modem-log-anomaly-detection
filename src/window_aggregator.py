from collections import deque

WINDOW_SIZE = 5
feature_window = deque(maxlen=WINDOW_SIZE)


def add_to_window(feature_dict):
    feature_window.append(feature_dict)


def aggregate_window():
    aggregated = {
        "error_count": 0,
        "warn_count": 0,
        "packet_loss_count": 0,
        "timeout_count": 0
    }

    for f in feature_window:
        for key in aggregated:
            aggregated[key] += f.get(key, 0)

    return aggregated
