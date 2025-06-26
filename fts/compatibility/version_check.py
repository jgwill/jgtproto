"""Version compatibility checking for jgtpy/jgtml integration."""

from dataclasses import dataclass
from typing import Optional, List, Dict
import importlib.metadata

@dataclass
class CompatibilityCheck:
    package: str
    required_min: str
    required_max: Optional[str]
    current: Optional[str]
    compatible: bool
    message: str


class VersionValidator:
    """Validate package versions for FTS integration."""

    COMPATIBILITY_MATRIX: Dict[str, Dict[str, Optional[str]]] = {
        'jgtpy': {'min': '1.2.0', 'max': '2.0.0'},
        'jgtml': {'min': '0.8.0', 'max': '1.0.0'},
        'click': {'min': '8.0.0', 'max': None},
    }

    def validate_environment(self) -> List[CompatibilityCheck]:
        results = []
        for package, cfg in self.COMPATIBILITY_MATRIX.items():
            try:
                current = importlib.metadata.version(package)
            except importlib.metadata.PackageNotFoundError:
                results.append(CompatibilityCheck(
                    package, cfg['min'], cfg['max'], None, False,
                    f"❌ Package not installed (pip install {package})"
                ))
                continue
            compatible = self._check_range(current, cfg['min'], cfg['max'])
            msg = "✅ Compatible" if compatible else f"❌ Version conflict (need >={cfg['min']})"
            results.append(CompatibilityCheck(
                package, cfg['min'], cfg['max'], current, compatible, msg
            ))
        return results

    def _check_range(self, current: str, min_ver: str, max_ver: Optional[str]) -> bool:
        from packaging import version
        cur_v = version.parse(current)
        if cur_v < version.parse(min_ver):
            return False
        if max_ver and cur_v >= version.parse(max_ver):
            return False
        return True
