from sqlalchemy import create_engine, update
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, Session
from sqlalchemy.orm import registry, mapped_column

from data.config import logger, ConfigSingleton

config = ConfigSingleton('.env')
url = config.db.get_url()
engine = create_engine(url, echo=True)

reg = registry()


class Base(MappedAsDataclass, DeclarativeBase):
    pass
