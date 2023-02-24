from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.db_connect import reg


@reg.mapped_as_dataclass
class Team:
    __tablename__ = "teams"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str]
    logo_path: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        insert_default=func.now(),
        default=None
    )
    updated_at: Mapped[datetime] = mapped_column(
        insert_default=func.now(),
        default=None
    )
