import pandas as pd
import networkx as nx
import os
import pickle

def load_berlin_data():
    path = "data/processed/berlin/urban_dashboard.csv"
    df = pd.read_csv(path)

    df["avg_travel_time"] = pd.to_timedelta(df["avg_travel_time"])
    df["minutes"] = df["avg_travel_time"].dt.total_seconds() / 60

    return df


def build_graph(df):
    G = nx.DiGraph()

    for _, row in df.iterrows():
        from_stop = row["from_stop"]
        to_stop = row["to_stop"]
        weight = row["minutes"]
        mode = row["mode"]

        G.add_edge(
            from_stop,
            to_stop,
            weight=weight,
            mode=mode,
            route=row["route_short_name"]
        )

    return G


def save_graph(G):
    path = "data/processed/berlin/graph.gpickle"
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "wb") as f:
        pickle.dump(G, f)

    print(f"\nGraph saved at: {path}")


if __name__ == "__main__":
    print("Script is running...")

    df = load_berlin_data()
    G = build_graph(df)

    print(f"Total Nodes (Stops): {len(G.nodes)}")
    print(f"Total Edges (Connections): {len(G.edges)}")

    save_graph(G)