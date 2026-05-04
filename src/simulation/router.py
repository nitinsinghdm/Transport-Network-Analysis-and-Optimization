from journey_simulator import evaluate_route
import networkx as nx
import pickle

def load_graph():
    
    path = "data/processed/berlin/graph.gpickle"

    with open(path, "rb") as f:
        G = pickle.load(f)

    print("Graph loaded")
    print(f"Total Nodes: {len(G.nodes)}")
    print(f"Total Edges: {len(G.edges)}")

    return G


def find_stop(G, keyword):
    matches = [node for node in G.nodes if keyword.lower() in node.lower()]

    if not matches:
        print(f"\nNo match found for: {keyword}")
        return None

    print(f"\nMatches for '{keyword}':")
    for i, m in enumerate(matches[:10]):
        print(f"{i}: {m}")

    while True:
        choice = input("Select index: ")

        if choice.isdigit():
            choice = int(choice)
            if 0 <= choice < len(matches):
                return matches[choice]

        print("Invalid input, enter a number like 0, 1, 2...")


def get_top_k_routes(G, source, target, k=3):
    print("\nFinding routes...")

    try:
        path_generator = nx.shortest_simple_paths(
            G,
            source=source,
            target=target,
            weight="weight"
        )

        paths = []
        for i, path in enumerate(path_generator):
            paths.append(path)
            if i + 1 == k:
                break

    except nx.NodeNotFound as e:
        print(f"\nError: {e}")
        return []

    except nx.NetworkXNoPath:
        print("\nNo path found between stops")
        return []

    return paths


def compute_route_metrics(G, path):
    total_time = 0
    modes = []

    for i in range(len(path) - 1):
        edge_data = G[path[i]][path[i + 1]]
        total_time += edge_data.get("weight", 0)
        modes.append(edge_data.get("mode", "Unknown"))

    transfers = len(set(modes)) - 1

    return total_time, transfers, modes


def print_routes(G, routes):
    if not routes:
        print("\nNo routes found")
        return

    print("\n" + "="*50)
    print("ROUTE COMPARISON")
    print("="*50)

    for i, path in enumerate(routes):
        metrics = evaluate_route(G, path, simulations=200)

        print(f"\nRoute {i+1}")
        print("-"*50)
        print("Path:")
        print(" → ".join(path))

        print("\nMetrics:")
        print(f"  Expected Time   : {metrics['expected_time']} min")
        print(f"  Variability     : {metrics['variability']}")
        print(f"  Delay Risk      : {metrics['delay_risk']}")
        print(f"  Reliability     : {metrics['reliability']}")
        print(f"  Missed Conn.    : {metrics['missed_connections']}")


if __name__ == "__main__":
    print("Script is running...")

    G = load_graph()

    source = find_stop(G, "Zoo")
    target = find_stop(G, "Alexanderplatz")

    if source and target:
        routes = get_top_k_routes(G, source, target, k=3)
        print_routes(G, routes)