from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="FTS Visualization API")

class TrendData(BaseModel):
    label: str
    trend: str

@app.get("/trends", response_model=List[TrendData])
async def get_trends() -> List[TrendData]:
    """Return mock trend data for visualization."""
    return [
        TrendData(label="M1", trend="Bullish"),
        TrendData(label="W1", trend="Bullish"),
        TrendData(label="D1", trend="Bearish"),
        TrendData(label="H1", trend="Bearish"),
        TrendData(label="m15", trend="Bearish"),
        TrendData(label="m1", trend="Bearish"),
    ]

class MFIItem(BaseModel):
    timestamp: str
    mfi: float
    mfi_sq: int
    mfi_green: int
    mfi_fade: int
    mfi_fake: int

@app.get("/mfi", response_model=List[MFIItem])
async def get_mfi() -> List[MFIItem]:
    """Return mock MFI signal data."""
    import pandas as pd
    import numpy as np
    index = pd.date_range("2024-01-01", periods=10, freq="D")
    return [
        MFIItem(
            timestamp=str(ts),
            mfi=float(np.random.uniform(40, 60)),
            mfi_sq=int(np.random.choice([0,1])),
            mfi_green=int(np.random.choice([0,1])),
            mfi_fade=int(np.random.choice([0,1])),
            mfi_fake=int(np.random.choice([0,1]))
        )
        for ts in index
    ]

