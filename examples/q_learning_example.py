"""Example training loop for the QLearningAgent."""

import random
from fts.rl import QLearningAgent

ACTIONS = ("buy", "sell", "hold")

# simple environment placeholder
STATES = [0, 1]
TRANSITIONS = {
    0: {"buy": (1, 1.0), "sell": (0, -1.0), "hold": (0, 0.0)},
    1: {"buy": (1, -1.0), "sell": (0, 1.0), "hold": (1, 0.0)},
}


def main(episodes: int = 1000):
    agent = QLearningAgent(ACTIONS)
    state = random.choice(STATES)
    for _ in range(episodes):
        action = agent.select_action(state)
        next_state, reward = TRANSITIONS[state][action]
        agent.update(state, action, reward, next_state)
        state = next_state
    for s in STATES:
        print(f"State {s}: {agent.q_table[s]}")


if __name__ == "__main__":
    main()
