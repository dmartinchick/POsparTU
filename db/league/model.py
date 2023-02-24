from datetime import datetime
from typing import List

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.db_connect import reg
from db.association_table.match_league import association_match_league_table


@reg.mapped_as_dataclass
class League:
    __tablename__ = "leagues"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    name_ru: Mapped[str]
    logo_path: Mapped[str] = mapped_column(nullable=True)
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(
        insert_default=func.now(), default=None
    )
    updated_at: Mapped[datetime] = mapped_column(
        insert_default=func.now(), default=None
    )
