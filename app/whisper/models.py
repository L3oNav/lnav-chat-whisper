from app.settings.base_models import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Script(Base):
    __tablename__ = "script"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    script = Column(String, nullable=False)
    language = Column(String, nullable=False)
    message_id = Column(UUID(as_uuid=True), ForeignKey('messages.id'), nullable=False)

    created_at = Column(DateTime, nullable=False, server_default="now()")
    updated_at = Column(DateTime, nullable=False, server_default="now()", onupdate="now()")
    message = relationship("Message", back_populates="script")
