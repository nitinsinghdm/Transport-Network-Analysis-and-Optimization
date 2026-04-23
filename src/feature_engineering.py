import pandas as pd

def convert_time(df):
    df["arrival_time_td"] = pd.to_timedelta(df["arrival_time"])
    return df

def compute_time_diff(df):
    df = df.sort_values(["trip_id", "stop_sequence"])
    df["time_diff"] = df.groupby("trip_id")["arrival_time_td"].diff()
    return df

def filter_valid_times(df):
    return df[
        (df["time_diff"] > pd.Timedelta(seconds=20)) &
        (df["time_diff"] <= pd.Timedelta(minutes=60))
    ]