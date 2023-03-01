from abc import ABC, abstractmethod
from db.sessions import Session
from db.specification import Specification


class Repository(ABC):

    def __init__(self, session: Session):
        self.session = session

    @abstractmethod
    def get(self, spec: Specification | None):
        raise NotImplementedError

    @abstractmethod
    def list(self, spec: Specification | None):
        raise NotImplementedError

    @abstractmethod
    def save(self, obj):
        raise NotImplementedError

    @abstractmethod
    def update(self, obj):
        raise NotImplementedError
