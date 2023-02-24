from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, relationship

from db.db_connect import reg


association_match_league_table = Table(
    "association_match_league_table",
    reg.metadata,
    Column("match_id", ForeignKey("matches.id"), primary_key=True),
    Column("league_id", ForeignKey("leagues.id"), primary_key=True)
)
