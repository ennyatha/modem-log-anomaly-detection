from sklearn.ensemble import IsolationForest


def train_model(feature_dict):
    feature_vector = [[
        feature_dict.get("error_count", 0),
        feature_dict.get("warn_count", 0),
        feature_dict.get("packet_loss_count", 0),
        feature_dict.get("timeout_count", 0)
    ]]

    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(feature_vector)

    return model


def predict_anomaly(model, feature_dict):
    feature_vector = [[
        feature_dict.get("error_count", 0),
        feature_dict.get("warn_count", 0),
        feature_dict.get("packet_loss_count", 0),
        feature_dict.get("timeout_count", 0)
    ]]

    prediction = model.predict(feature_vector)
    return prediction[0] == -1
