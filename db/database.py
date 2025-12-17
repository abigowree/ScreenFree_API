from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_USERNAME = "postgres"
DB_PASSWORD = "Abi%402007-5"
DB_HOSTNAME = "localhost"
DATABASE = "screenfree"
DB_PORT = "5432"

DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}:{DB_PORT}/{DATABASE}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

