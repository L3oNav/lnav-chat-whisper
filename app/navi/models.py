from app.settings.base_models import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Message(Base):

    __tablename__ = 'messages'

    id = Column(UUID(as_uuid=True) , primary_key=True, default=uuid.uuid4)
    sender_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    receiver_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    message = Column(String, nullable=False)
    attachment = Column(Boolean, nullable=False, default=False)
    attachment_url = Column(String, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default="now()")
    updated_at = Column(DateTime, nullable=False, server_default="now()", onupdate="now()")
    user = relationship("User", back_populates="messages")

class Reactions(Base):
    
    __tablename__ = 'reactions'
    
    id = Column(UUID(as_uuid=True) , primary_key=True, default=uuid.uuid4)
    message_id = Column(UUID(as_uuid=True), ForeignKey('messages.id'), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    reaction = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default="now()")
    updated_at = Column(DateTime, nullable=False, server_default="now()", onupdate="now()")
    message = relationship("Message", back_populates="reactions")

