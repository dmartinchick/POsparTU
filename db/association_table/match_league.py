from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, relationship

from db.db_connect import reg, Base
# from db.match.model import Match
# from db.league.model import League

association_match_league_table = Table(
    "association_match_league_table",
    reg.metadata,
    Column("match_id", ForeignKey("matches.id"), primary_key=True),
    Column("league_id", ForeignKey("leagues.id"), primary_key=True)
)
"""
@reg.mapped_as_dataclass
class AssociationMatchLeague:
    __tablename__ = "association_match_league_table"

    match_id: Mapped[int] = relationship(ForeignKey("matches.id"))
    league_id"""