from datetime import datetime
from typing import List

from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.db_connect import reg
from db.league.model import League
from db.association_table.match_league import association_match_league_table


@reg.mapped_as_dataclass
class Match:
    __tablename__ = 'matches'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    home_team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))
    visitor_team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))
    leagues: Mapped[List[League]] = relationship(secondary=association_match_league_table)
    home_team: Mapped["Team"] = relationship(foreign_keys=[home_team_id])
    visitor_team: Mapped["Team"] = relationship(foreign_keys=[visitor_team_id])
    vote_count: Mapped[int] = mapped_column(default=0)
    is_choosen: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(
        insert_default=func.now(), default=None
    )
    updated_at: Mapped[datetime] = mapped_column(
        insert_default=func.now(), default=None
    )
