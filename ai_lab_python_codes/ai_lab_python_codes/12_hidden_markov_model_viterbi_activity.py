"""Hidden Markov Model — Activity Recognition using Viterbi-style scoring.

Install dependency with: python -m pip install numpy
"""

import numpy as np

STATES = ["Idle", "Walking", "Running"]
OBSERVATIONS = ["low", "medium", "high"]
TRANSITION = np.array([
    [0.6, 0.3, 0.1],
    [0.2, 0.6, 0.2],
    [0.1, 0.3, 0.6],
])
EMISSION = np.array([
    [0.7, 0.2, 0.1],
    [0.2, 0.5, 0.3],
    [0.1, 0.2, 0.7],
])
INITIAL = np.array([0.6, 0.3, 0.1])
OBSERVATION_SEQUENCE = ["low", "medium", "high"]


def viterbi_final_state(sequence):
    scores = INITIAL * EMISSION[:, OBSERVATIONS.index(sequence[0])]
    for observation in sequence[1:]:
        scores = np.max(scores[:, None] * TRANSITION, axis=0)
        scores *= EMISSION[:, OBSERVATIONS.index(observation)]
    return STATES[int(np.argmax(scores))]


if __name__ == "__main__":
    print("Predicted activity:", viterbi_final_state(OBSERVATION_SEQUENCE))
