"""Vector database client placeholders."""

from typing import Any

class VectorDBClient:
    """Generic interface for vector similarity search."""

    def __init__(self, url: str):
        self.url = url

    def upsert(self, vector_id: str, embedding: list[float]) -> None:
        """Store an embedding."""
        raise NotImplementedError

    def query(self, embedding: list[float], k: int = 10) -> Any:
        """Find nearest neighbors."""
        raise NotImplementedError
