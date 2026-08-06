# Connect FastAPI → SQLAlchemy → PostgreSQL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# PostgreSQL connection URL
DATABASE_URL = "postgresql://postgres:narayansharma@localhost:5432/demo"

# Create database connection
engine = create_engine(DATABASE_URL)


# Create database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Parent class for database models
Base = declarative_base()
