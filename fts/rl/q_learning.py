"""Simple Q-learning agent for demonstration purposes."""

from collections import defaultdict
from typing import Any, Tuple

class QLearningAgent:
    """Tabular Q-learning agent."""

    def __init__(self, actions: Tuple[Any, ...], alpha: float = 0.1, gamma: float = 0.99, epsilon: float = 0.1):
        self.actions = actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = defaultdict(lambda: {a: 0.0 for a in actions})

    def select_action(self, state: Any) -> Any:
        import random
        if random.random() < self.epsilon:
            return random.choice(self.actions)
        q_values = self.q_table[state]
        return max(q_values, key=q_values.get)

    def update(self, state: Any, action: Any, reward: float, next_state: Any) -> None:
        next_q = max(self.q_table[next_state].values(), default=0.0)
        old_q = self.q_table[state][action]
        self.q_table[state][action] = old_q + self.alpha * (reward + self.gamma * next_q - old_q)
