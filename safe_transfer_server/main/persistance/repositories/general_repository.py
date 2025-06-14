from typing import Type, TypeVar, Generic, List, Optional
from uuid import UUID

from sqlalchemy.orm import Session

from safe_transfer_server.main.persistance.config.database_connection import Base

Entity = TypeVar('Entity', bound=Base)


class GeneralRepository(Generic[Entity]):
    def __init__(self, session: Session, model: Type[Entity]):
        self.session = session
        self.model = model

    def get_all(self) -> List[Entity]:
        return self.session.query(self.model).all()

    def get_by_id(self, id: UUID) -> Optional[Entity]:
        return self.session.get(self.model, id)

    def create(self, entity: Entity) -> Entity:
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity

    def update(self, entity: Entity) -> Entity:
        self.session.merge(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity

    def delete(self, id: UUID) -> Optional[Entity]:
        obj = self.get_by_id(id)
        if obj:
            self.session.delete(obj)
            self.session.commit()
        return obj
