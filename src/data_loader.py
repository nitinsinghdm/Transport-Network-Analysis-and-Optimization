import pandas as pd
import os

BASE_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "raw")

def load_dataset(dataset="germany"):
    dataset_path = os.path.join(BASE_PATH, dataset)

    return {
        "stops": pd.read_csv(os.path.join(dataset_path, "stops.txt"), low_memory=False),
        "stop_times": pd.read_csv(os.path.join(dataset_path, "stop_times.txt"), low_memory=False),
        "trips": pd.read_csv(os.path.join(dataset_path, "trips.txt"), low_memory=False),
        "routes": pd.read_csv(os.path.join(dataset_path, "routes.txt"), low_memory=False)
    }