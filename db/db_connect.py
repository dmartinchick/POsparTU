from sqlalchemy import create_engine
from sqlalchemy.orm import registry, DeclarativeBase
from sqlalchemy.orm.session import sessionmaker

from data.config import logger, ConfigSingleton


reg = registry()

config = ConfigSingleton('.env')
url = config.db.get_url()
engine = create_engine(url, echo=True)

# Base = declarative_base(engine)
# Sessiom = sessionmaker(engine)
