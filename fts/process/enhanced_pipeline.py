"""Enhanced FTS process with comprehensive error handling."""

import asyncio
import logging
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Optional, List


class PipelineStage(Enum):
    DATA_ACQUISITION = "data_acquisition"
    SIGNAL_PROCESSING = "signal_processing"
    PATTERN_RECOGNITION = "pattern_recognition"
    SIGNAL_VALIDATION = "signal_validation"
    DECISION_MAKING = "decision_making"
    EXECUTION = "execution"
    MONITORING = "monitoring"


@dataclass
class StageResult:
    stage: PipelineStage
    success: bool
    data: Optional[Any] = None
    error: Optional[str] = None
    duration_ms: Optional[float] = None
    retry_count: int = 0


class ResilientEnhancedFTSPipeline:
    """Enhanced pipeline with retry and fallback logic."""

    def __init__(self, config: Optional[Dict] = None):
        self.config = config or self._default_config()
        self.logger = logging.getLogger(__name__)
        self._setup_services()

    def _default_config(self) -> Dict:
        return {
            'max_retries': 3,
            'timeout_seconds': 30,
            'fallback_enabled': True,
        }

    def _setup_services(self):
        try:
            import jgtpy
            self.cds = jgtpy.cds_create()
            self.ads = jgtpy.ads_create()
            self.jgtpy_ok = True
        except Exception as exc:  # broad for environment w/out packages
            self.logger.warning(f'jgtpy unavailable: {exc}')
            self.jgtpy_ok = False

        try:
            from jgtml.alligator_cli import AlligatorProcessor
            from jgtml.fdbscan import FractalDBScan
            self.alligator = AlligatorProcessor()
            self.fdbscan = FractalDBScan()
            self.jgtml_ok = True
        except Exception as exc:
            self.logger.warning(f'jgtml unavailable: {exc}')
            self.jgtml_ok = False

    async def execute_with_resilience(self, symbol: str, timeframes: List[str]) -> Dict[str, StageResult]:
        results: Dict[str, StageResult] = {}
        previous_data = None
        for stage in [
            PipelineStage.DATA_ACQUISITION,
            PipelineStage.SIGNAL_PROCESSING,
            PipelineStage.PATTERN_RECOGNITION,
            PipelineStage.SIGNAL_VALIDATION,
            PipelineStage.DECISION_MAKING,
            PipelineStage.EXECUTION,
            PipelineStage.MONITORING,
        ]:
            func = getattr(self, f'_stage_{stage.value}')
            result = await self._run_stage(stage, func, symbol, timeframes, previous_data)
            results[stage.value] = result
            if not result.success and not self.config['fallback_enabled']:
                break
            previous_data = result.data
        return results

    async def _run_stage(self, stage: PipelineStage, func, symbol: str, timeframes: List[str], prev: Any) -> StageResult:
        start = asyncio.get_event_loop().time()
        for attempt in range(self.config['max_retries']):
            try:
                data = await asyncio.wait_for(func(symbol, timeframes, prev), self.config['timeout_seconds'])
                duration = (asyncio.get_event_loop().time() - start) * 1000
                return StageResult(stage, True, data, duration_ms=duration, retry_count=attempt)
            except asyncio.TimeoutError:
                err = f'{stage.value} timed out'
            except Exception as exc:
                err = f'{stage.value} error: {exc}'
            self.logger.warning(f"{err}, retry {attempt+1}")
            await asyncio.sleep(2 ** attempt)
        return StageResult(stage, False, error=err, retry_count=self.config['max_retries'])

    async def _stage_data_acquisition(self, symbol: str, timeframes: List[str], _: Any):
        if self.jgtpy_ok:
            try:
                return await self.cds.get_multi_timeframe_data(symbol, timeframes)
            except Exception as exc:
                self.logger.warning(f"cds failed: {exc}")
        return {'symbol': symbol, 'timeframes': timeframes, 'data': []}

    async def _stage_signal_processing(self, symbol: str, timeframes: List[str], data: Any):
        if self.jgtpy_ok and data:
            try:
                return await self.ads.process_advanced_signals(data)
            except Exception as exc:
                self.logger.warning(f"ads failed: {exc}")
        return {}

    async def _stage_pattern_recognition(self, symbol: str, timeframes: List[str], data: Any):
        if self.jgtml_ok and data:
            try:
                return self.fdbscan.detect_fractal_patterns(data)
            except Exception as exc:
                self.logger.warning(f"fdbscan failed: {exc}")
        return []

    async def _stage_signal_validation(self, symbol: str, timeframes: List[str], data: Any):
        if self.jgtml_ok and data:
            try:
                return self.alligator.validate_trading_signals(data)
            except Exception as exc:
                self.logger.warning(f"alligator failed: {exc}")
        return []

    async def _stage_decision_making(self, symbol: str, timeframes: List[str], data: Any):
        return data

    async def _stage_execution(self, symbol: str, timeframes: List[str], data: Any):
        return data

    async def _stage_monitoring(self, symbol: str, timeframes: List[str], data: Any):
        return data
