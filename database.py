import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings 





# POSTGRES_URL = f"{settings.POSTGRES_URL}"

# Deployment.

POSTGRES_URL = os.environ.get('POSTGRES_URL')



engine = create_engine(POSTGRES_URL, echo=True, pool_size=10, max_overflow=20)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


