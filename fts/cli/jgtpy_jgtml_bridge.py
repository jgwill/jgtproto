"""CLI bridge weaving jgtpy and jgtml into executable workflows."""

import asyncio
from typing import List

import click

try:
    import jgtpy
    from jgtml.alligator_cli import AlligatorProcessor
    from jgtml.fdbscan import FractalDBScan
except ImportError:
    jgtpy = None
    AlligatorProcessor = None
    FractalDBScan = None

@click.group()
@click.version_option()
def fts_cli():
    """Enhanced FTS CLI with jgtpy/jgtml integration."""
    pass

@fts_cli.command()
@click.option('--symbol', required=True, help='Trading symbol (e.g., EURUSD)')
@click.option('--timeframes', multiple=True, default=['H1'], help='Timeframes to analyze')
@click.option('--confidence', default=0.75, help='Signal confidence threshold')
@click.option('--output-format', type=click.Choice(['json', 'csv', 'pretty']), default='pretty')
def scan_and_validate(symbol: str, timeframes: tuple, confidence: float, output_format: str):
    """Execute complete jgtpy→jgtml signal scanning and validation."""
    asyncio.run(_execute_scan_validate(symbol, list(timeframes), confidence, output_format))


async def _execute_scan_validate(symbol: str, timeframes: List[str], confidence: float, output_format: str):
    """Async execution with proper error handling."""
    if jgtpy is None or AlligatorProcessor is None:
        click.echo('❌ Required packages jgtpy/jgtml not installed')
        return
    try:
        cds = jgtpy.cds_create()
        market_data = await cds.get_multi_timeframe_data(symbol, timeframes)
        if not market_data:
            click.echo(f"❌ No market data available for {symbol}")
            return
        ads = jgtpy.ads_create()
        processed_signals = await ads.process_advanced_signals(market_data)
        fdbscan = FractalDBScan()
        patterns = fdbscan.detect_fractal_patterns(processed_signals)
        alligator = AlligatorProcessor()
        validated = alligator.validate_trading_signals(patterns, confidence_threshold=confidence)
        _output_results(validated, output_format, symbol, timeframes)
    except jgtpy.ConnectionError as e:  # type: ignore[attr-defined]
        click.echo(f"❌ jgtpy connection failed: {e}")
    except Exception as e:
        click.echo(f"❌ Unexpected error: {e}")


def _output_results(signals, fmt: str, symbol: str, timeframes: List[str]):
    if fmt == 'json':
        import json
        click.echo(json.dumps([s.to_dict() for s in signals], indent=2))
    else:
        click.echo(f"\n🎯 {symbol} Analysis Results ({', '.join(timeframes)})")
        click.echo(f"📊 Signals processed: {len(signals)}")
        for i, s in enumerate(signals, 1):
            click.echo(f"  {i}. Confidence: {getattr(s, 'confidence', 0):.2f}")


if __name__ == '__main__':
    fts_cli()
