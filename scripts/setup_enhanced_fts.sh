#!/bin/bash
# 🌸 Miette says: "Let's make this setup feel like magic, not work!"

echo "🌀 Setting up Enhanced FTS with jgtpy/jgtml integration..."

# Version validation
python - <<'PY'
from fts.compatibility.version_check import VersionValidator
validator = VersionValidator()
results = validator.validate_environment()
all_ok = True
for r in results:
    print(f"{r.message} {r.package} ({r.current or 'missing'})")
    if not r.compatible:
        all_ok = False
if not all_ok:
    print('\n❌ Some packages need attention. Run:')
    print('pip install --upgrade jgtpy jgtml click packaging')
    exit(1)
else:
    print('\n✅ All packages compatible! Ready to trade! 🚀')
PY

# Test CLI installation
python -m fts.cli.jgtpy_jgtml_bridge --help >/dev/null

echo "✨ Setup complete! Try: python -m fts.cli.jgtpy_jgtml_bridge scan-and-validate --symbol EURUSD"
