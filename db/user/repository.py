from sqlalchemy.exc import NoResultFound

from db.exeptions import NotFoundExeption
from db.repository import Repository
from db.user.model import User


class UserRepository(Repository):
    def get(self, spec: Specification):
        try:
            self.session.query(User).filter(spec).one()
        except NoResultFound as exc:
            raise NotFoundExeption(exc)

    def list(self, spec: Specification):
        try:
            self.session.query(User).filter(spec).all()
        except NoResultFound as exc:
            raise NotFoundExeption(exc)

    def save(self, obj):
        self.session.add(obj)

    def update(self, obj):
        self.session.add(obj)
