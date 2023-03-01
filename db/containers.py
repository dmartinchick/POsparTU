from db.sessions import Session
from db.user.model import User
from db.unit_of_work import AlchemyUnitOfWork
from db.user.repository import UserRepository


class Container:

    session_creator = Session()
    users_repository = UserRepository(session=session_creator)
    users_uow = AlchemyUnitOfWork(repository=users_repository)
