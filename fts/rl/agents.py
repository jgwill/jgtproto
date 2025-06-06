"""Reinforcement learning agent definitions."""

from typing import Any

class BaseRLAgent:
    """Simple RL agent placeholder."""

    def __init__(self, state_space: Any, action_space: Any):
        self.state_space = state_space
        self.action_space = action_space

    def act(self, state: Any) -> Any:
        """Return an action for a given state."""
        raise NotImplementedError

    def learn(self, reward: float, next_state: Any) -> None:
        """Update the agent based on reward."""
        raise NotImplementedError
