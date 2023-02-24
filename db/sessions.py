from sqlalchemy.orm import sessionmaker
from db.db_connect import engine

Session = sessionmaker(bind=engine)
