from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Factory

from db.sessions import Session
from db.unit_of_work import AlchemyUnitOfWork
from db.user.repository import UserRepository


class Container(DeclarativeContainer):
    wiring_config = WiringConfiguration(
        packages=[
            'users',
        ]
    )

    session_creator = Factory(Session)

    users_repository = Factory(
        UserRepository,
        session=session_creator
    )

    users_uow = Factory(
        AlchemyUnitOfWork,
        repository=users_repository
    )
