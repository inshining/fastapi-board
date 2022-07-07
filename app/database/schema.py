from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    func,
    Enum,
    Boolean,
    ForeignKey,
)
from sqlalchemy.orm import Session, relationship

from app.database.conn import Base, db

class BaseMixin:
    id = Column(Integer, primary_key = True, index=True)
    created_at = Column(DateTime, nullabe=False, default=func.utc_timestamp())
    updated_at = Column(DateTime, nullabe=False, default=func.utc_timestamp(), onupdate=func.utc_timestamp())

    def __int__(self):
        self._q = None
        self._session = None
        self.served = None

