import random

# mean delay (minutes), std deviation
DELAY_CONFIG = {
    "Bus": (1.5, 1.0),
    "S-Bahn": (2.0, 1.5),
    "U-Bahn": (1.0, 0.7)
}

TRANSFER_TIME = 3  # minutes


def sample_delay(mode):
    mean, std = DELAY_CONFIG.get(mode, (1.0, 1.0))
    delay = random.gauss(mean, std)

    return max(0, delay)  # no negative delays


def transfer_penalty():
    return TRANSFER_TIME


def miss_connection_probability(delay):
    if delay < 2:
        return 0.05
    elif delay < 5:
        return 0.15
    else:
        return 0.35