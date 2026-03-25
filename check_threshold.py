#!/usr/bin/env python
# coding: utf-8

import os
import mlflow

# Use environment variable if available, else default to local mlflow.db
mlflow_uri = os.environ.get("MLFLOW_URI", "sqlite:///mlflow.db")
mlflow.set_tracking_uri(mlflow_uri)

# Read Run ID
with open("model_info.txt") as f:
    run_id = f.read().strip()

# Get the run from MLflow
run = mlflow.get_run(run_id)
accuracy = run.data.metrics.get("val_accuracy", 0.0)

print(f"Validation Accuracy: {accuracy}")
if accuracy < 0.85:
    raise ValueError(f"Accuracy {accuracy} below threshold! Deployment stopped.")
else:
    print("Accuracy threshold met. Deployment can proceed.")