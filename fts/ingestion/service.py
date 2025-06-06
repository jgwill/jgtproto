"""AsyncIO-based ingestion service placeholder."""

import asyncio
from typing import Iterable, Awaitable

class IngestionService:
    """Collects data from multiple async sources and forwards to storage."""

    def __init__(self, sources: Iterable[Awaitable]):
        self.sources = list(sources)

    async def run(self) -> None:
        """Start all source tasks and wait for completion."""
        tasks = [asyncio.create_task(src) for src in self.sources]
        await asyncio.gather(*tasks)
