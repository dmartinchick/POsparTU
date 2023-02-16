from sqlalchemy import create_engine
from sqlalchemy.orm import registry
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from data.config import load_config

reg = registry()

config = load_config('.env')
url = config.db.get_url()
engine = create_engine(url, echo=True)

Base = declarative_base(engine)
Sessiom = sessionmaker(engine)
