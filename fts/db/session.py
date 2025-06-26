from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

ENGINE_URL = "sqlite:///fts.db"  # placeholder, replace with QuestDB or other

engine = create_engine(ENGINE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)


def init_db() -> None:
    from .models import Base

    Base.metadata.create_all(engine)
