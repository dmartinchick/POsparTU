from datetime import datetime

from sqlalchemy.orm import Session

from db.db_connect import reg, engine
from db.association_table.match_league import association_match_league_table
from db.league.model import League
from db.match.model import Match
from db.result.model import Result
from db.team.model import Team
from db.bet.model import Bet
from db.user.model import User


def created_all():
    reg.metadata.create_all(engine)


def add_user(id: int, first_name: str, last_name: str, is_admin: bool = 0, is_superuser: bool = 0):
    with Session(engine) as session:
        user = User(
            id=id,
            first_name=first_name,
            last_name=last_name,
            is_admin=is_admin,
            is_superuser=is_superuser
        )
        session.add(user)
        session.commit()


def update_user(id_updated_user: int):
    with Session(engine) as session:
        updated_user = session.query(User).filter(User.id == id_updated_user).one()
        updated_user.is_admin = True
        updated_user.is_superuser = True
        updated_user.update_at = datetime.utcnow()
        session.commit()
