from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, DateTime

class Base(DeclarativeBase):
    # Generate __tablename__ automatically

    created_at = Column(DateTime, nullable=False, server_default="now()")
    updated_at = Column(DateTime, nullable=False, server_default="now()", onupdate="now()")
