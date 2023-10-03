from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_dsn = settings.DB_DSN

engine = create_engine(db_dsn)
Session = sessionmaker(bind=engine)


def get_session():
    return Session()