from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Having this attribute is guaranteed by Pydantic, so no reason to listen to mypy here
engine = create_engine(settings.DATABASE_URI, pool_pre_ping=True)  # type: ignore
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@as_declarative()
class BaseModel:
    pass
