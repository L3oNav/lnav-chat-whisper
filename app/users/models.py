from app.settings.base_model import Model
from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

class User(Model):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String(50))
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=True, default=None)
    accounts = relationship("Account", back_populates="user")
