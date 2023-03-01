from db.user.model import User
from db.user.specification import UserByIdSpecification, IsActiveUserSpecification, IsSuperuserSpecification
from db.user.services import get_user, list_users, add_user, update_user
from db.sessions import Session
from db.containers import Container
from data.config import logger


def get_superusers_list(container: Container) -> list:
    is_active_users_specification = IsActiveUserSpecification().is_satisfied(True)
    is_superusers_specification = IsSuperuserSpecification().is_satisfied(True)
    spec = is_superusers_specification & is_active_users_specification
    logger.info(container.users_repository)

    return list_users(spec, repository=container.users_repository)


def get_all_active_users(container: Container) -> list:
    spec = IsActiveUserSpecification().is_satisfied(True)
    return list_users(spec=spec, repository=container.users_repository)


def get_user_by_id(user_id: int, container: Container) -> User:
    spec = UserByIdSpecification().is_satisfied(user_id)
    return get_user(spec, container.users_repository)
