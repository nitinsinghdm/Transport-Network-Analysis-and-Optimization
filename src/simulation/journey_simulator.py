import random
import numpy as np
from .delay_model import (
    sample_delay,
    transfer_penalty,
    miss_connection_probability
)


def simulate_route(G, path):
    total_time = 0
    modes = []
    missed_connections = 0

    for i in range(len(path) - 1):
        edge = G[path[i]][path[i + 1]]

        base_time = edge.get("weight", 0)
        mode = edge.get("mode", "Bus")

        delay = sample_delay(mode)

        total_time += base_time + delay
        modes.append(mode)

        # transfer check
        if i > 0:
            prev_mode = modes[i - 1]

            if mode != prev_mode:
                total_time += transfer_penalty()

                prob = miss_connection_probability(delay)

                if random.random() < prob:
                    missed_connections += 1
                    total_time += transfer_penalty()  # extra wait

    return total_time, missed_connections


def evaluate_route(G, path, simulations=300):
    results = []
    misses = []

    for _ in range(simulations):
        time, miss = simulate_route(G, path)
        results.append(time)
        misses.append(miss)

    avg_time = np.mean(results)
    std_time = np.std(results)
    delay_risk = np.mean([1 if t > avg_time else 0 for t in results])
    reliability = 1 / (1 + std_time)

    return {
        "expected_time": round(avg_time, 2),
        "variability": round(std_time, 2),
        "delay_risk": round(delay_risk, 2),
        "reliability": round(reliability, 3),
        "missed_connections": sum(misses)
    }