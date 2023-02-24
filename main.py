from datetime import datetime
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data.config import logger, ConfigSingleton
from handlers.echo import register_echo_handlers
from handlers.main_menu import register_main_menu_handlers
from handlers.admin_panel import register_admin_panel_handlers

from db.db_connect import Session, reg, engine, update, Base
from db.association_table.match_league import association_match_league_table
# from db.league.model import League
from db.user.model import User
from db.match.model import Match
from db.bet.model import Bet
from db.result.model import Result
from db.team.model import Team


def add_user(id: int, first_name: str, last_name: str):
    with Session(engine) as session:
        user = User(
            id=id,
            first_name=first_name,
            last_name=last_name,
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


def created_all():
    reg.metadata.create_all(engine)


@logger.catch
def main():
    config = ConfigSingleton(path='.env')
    bot = Bot(token=config.tg_bot.token)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    # register handlers
    register_echo_handlers(dp)
    register_main_menu_handlers(dp)
    register_admin_panel_handlers(dp)

    # created_all()
    # add_user(id=466138751, first_name="Дмитрий", last_name="Мартинчик")
    # update_user(466138751)
    # executor.start_polling(dp)


if __name__ == '__main__':
    main()
