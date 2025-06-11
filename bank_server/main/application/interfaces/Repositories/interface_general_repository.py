from abc import abstractmethod, ABC
from typing import Generic, TypeVar, List
from uuid import UUID

Entity: TypeVar = TypeVar('Entity')


class IGeneralRepository(Generic[Entity], ABC):
    @abstractmethod
    def get_all(self) -> List[Entity]:
        pass

    @abstractmethod
    def get_by_id(self, id: UUID) -> Entity:
        pass

    @abstractmethod
    def create(self, entity: Entity) -> Entity:
        pass

    @abstractmethod
    def update(self, entity: Entity) -> Entity:
        pass

    @abstractmethod
    def delete(self, id: UUID) -> Entity:
        pass

# docker run --name bank-service-db -e POSTGRES_DB=bank-service -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin -p 5432:5432 -v bank-pgdata:/var/lib/postgresql/data -d postgres:15
