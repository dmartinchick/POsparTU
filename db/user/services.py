from datetime import datetime
from dependency_injector.wiring import inject, Provide

from db.specification import Specification
from db.user.specification import UserByIdSpecification
from db.containers import Container
from db.exeptions import NotFoundExeption
from db.user.repository import Repository   # TODO: в примере просто Repository
from db.unit_of_work import UnitOfWork
from db.user.model import User


@inject
def list_users(spec: Specification,
               repository: Repository = Provide[Container.users_repository]):
    try:
        return repository.list(spec)
    except NotFoundExeption:
        return None


@inject
def get_user(spec: Specification,
             repository: Repository = Provide[Container.users_repository]):
    try:
        return repository.get(spec)
    except NotFoundExeption:
        return None


@inject
def add_user(
        user_id: int,
        first_name: str,
        last_name: str,
        unit_of_work: UnitOfWork = Provide[Container.users_uow]
):
    new_user = User(
        id=user_id,
        first_name=first_name,
        last_name=last_name
    )
    unit_of_work.repository.save(new_user)
    unit_of_work.commit()


@inject
def update_user(
        user_id: int,
        update_param: str,
        update_data: str | bool,
        unit_of_work: UnitOfWork = Provide[Container.users_uow]
):
    spec = UserByIdSpecification()
    user = unit_of_work.repository.get(spec.is_satisfied(user_id))
    if hasattr(user, update_param):
        user.__setattr__(update_param, update_data)
        user.update_at = datetime.now()
        unit_of_work.repository.update(user)
        unit_of_work.commit()
