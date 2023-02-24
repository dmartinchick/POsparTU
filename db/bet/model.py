from datetime import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.db_connect import reg


@reg.mapped_as_dataclass
class Bet:
    __tablename__ = "bets"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    users: Mapped["User"] = relationship()
    match_id: Mapped[int] = mapped_column(ForeignKey("matches.id"))
    matches: Mapped["Match"] = relationship()
    home_team_goals: Mapped[int] = mapped_column(nullable=False)
    visitor_team_goals: Mapped[int] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        insert_default=func.now(), default=None
    )
    updated_at: Mapped[datetime] = mapped_column(
        insert_default=func.now(), default=None
    )
