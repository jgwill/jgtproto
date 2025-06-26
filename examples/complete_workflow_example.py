"""Complete workflow example showing real usage patterns."""

import asyncio

from fts.process.enhanced_pipeline import ResilientEnhancedFTSPipeline
from fts.compatibility.version_check import VersionValidator


async def main():
    print("🔍 Validating environment...")
    validator = VersionValidator()
    issues = [r for r in validator.validate_environment() if not r.compatible]
    if issues:
        for r in issues:
            print(r.message)
        return
    print("✅ Environment validated!")
    pipeline = ResilientEnhancedFTSPipeline()
    print("\n🚀 Executing pipeline...")
    results = await pipeline.execute_with_resilience('EURUSD', ['H1', 'H4'])
    print("\n📈 Results:")
    for name, res in results.items():
        status = '✅' if res.success else '❌'
        print(f"{status} {name}: {res.error or 'ok'}")


if __name__ == '__main__':
    asyncio.run(main())
