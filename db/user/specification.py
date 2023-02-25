from db.user.model import User
from db.specification import Specification


class UserByIdSpecification(Specification):
    def is_satisfied(self, candidate: int):
        return User.id == candidate


class IsActiveUserSpecification(Specification):
    def is_satisfied(self, candidate: bool):
        return User.is_active == candidate


class IsAdminUserSpecification(Specification):
    def is_satisfied(self, candidate: bool):
        return User.is_admin == candidate


class IsSuperuserSpecification(Specification):
    def is_satisfied(self, candidate: bool):
        return User.is_superuser == candidate


class UserByFirstNameSpecificatin(Specification):
    def is_satisfied(self, candidate: str):
        return User.first_name == candidate


class UserByLastNameSpecification(Specification):
    def is_satisfied(self, candidate: str):
        return User.last_name == candidate
