import asyncio
from fts.cli.jgtpy_jgtml_bridge import _execute_scan_validate

async def main():
    await _execute_scan_validate('EURUSD', ['H1', 'H4'], 0.75, 'pretty')

if __name__ == '__main__':
    asyncio.run(main())
