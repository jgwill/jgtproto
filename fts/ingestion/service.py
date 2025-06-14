"""Asynchronous ingestion service with uvloop and retry logic."""

import asyncio
from typing import Iterable, Awaitable, Callable, Optional

try:  # prefer uvloop if installed
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except Exception:  # pragma: no cover - uvloop optional
    pass

class IngestionService:
    """Collects data from multiple async sources and forwards to storage."""

    def __init__(self, sources: Optional[Iterable[Callable[[], Awaitable]]] = None, retry: int = 3):
        self.source_factories = list(sources or [])
        self.retry = retry

    def add_source(self, factory: Callable[[], Awaitable]) -> None:
        """Register a new asynchronous feed factory."""
        self.source_factories.append(factory)

    async def _run_source(self, factory: Callable[[], Awaitable]) -> None:
        """Run a single source with simple retry logic."""
        attempts = 0
        while True:
            try:
                await factory()
                break
            except Exception as exc:  # pragma: no cover - integration only
                attempts += 1
                if attempts > self.retry:
                    raise
                await asyncio.sleep(min(2 ** attempts, 30))

    async def run(self) -> None:
        """Start all source tasks and wait for completion."""
        tasks = [asyncio.create_task(self._run_source(f)) for f in self.source_factories]
        await asyncio.gather(*tasks)


async def run_default() -> None:
    """Example entry point using environment configuration."""
    service = IngestionService()
    # TODO: add real source factories fetching data from exchanges
    async def dummy_source():
        await asyncio.sleep(0.1)

    service.add_source(dummy_source)
    await service.run()


if __name__ == "__main__":
    asyncio.run(run_default())
