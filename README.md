# Modem Log Anomaly Detection System (ML + Rule-Based)

## Overview
This project implements a hybrid **rule-based and machine learning anomaly detection pipeline** for cellular modem logs.  
It is designed to detect abnormal network behavior such as packet loss, timeouts, and error bursts over time.

The system simulates **real-world modem telemetry pipelines** used in large-scale wireless products (e.g., smartphones, IoT devices).

---

## Architecture
The pipeline follows a layered approach:

1. Log ingestion and parsing
2. Rule-based anomaly detection
3. Feature extraction
4. Sliding time window aggregation
5. Machine learning–based anomaly detection

---

## Components

### 1. Log Reader
Parses raw modem logs into structured events:
- Timestamp
- Severity level (INFO/WARN/ERROR)
- Message content

### 2. Rule-Based Detection
Detects immediate anomalies:
- Error spikes
- Packet loss events
- Timeout occurrences

### 3. Feature Extraction
Extracts numeric features from logs:
- error_count
- warn_count
- packet_loss_count
- timeout_count

### 4. Sliding Window Aggregation
Maintains a rolling window of recent feature snapshots to capture **temporal behavior**.

### 5. Machine Learning Model
Uses **Isolation Forest** (unsupervised learning) to:
- Learn normal modem behavior
- Detect anomalies over time without labeled data

---

## Why Isolation Forest?
- Works well with unlabeled telemetry data
- Efficient for real-time anomaly detection
- Commonly used in network monitoring system
