from __future__ import annotations

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()


class FractalPattern(Base):
    __tablename__ = "fractal_patterns"
    id = Column(Integer, primary_key=True)
    symbol = Column(String, index=True)
    timeframe = Column(String, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    pattern_type = Column(String)
    attributes = Column(String)
    indicators = relationship("IndicatorValue", back_populates="pattern")
    signals = relationship("TradeSignal", back_populates="pattern")


class IndicatorValue(Base):
    __tablename__ = "indicator_values"
    id = Column(Integer, primary_key=True)
    pattern_id = Column(Integer, ForeignKey("fractal_patterns.id"))
    name = Column(String)
    value = Column(Float)
    pattern = relationship("FractalPattern", back_populates="indicators")


class TradeSignal(Base):
    __tablename__ = "trade_signals"
    id = Column(Integer, primary_key=True)
    pattern_id = Column(Integer, ForeignKey("fractal_patterns.id"))
    decision = Column(String)
    confidence = Column(Float)
    pattern = relationship("FractalPattern", back_populates="signals")
