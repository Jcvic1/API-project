from database import Base
from sqlalchemy import TIMESTAMP, Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    notes = relationship("Note", back_populates="owner", cascade="all, delete-orphan")
    api_keys = relationship("APIKey", back_populates="owner", cascade="all, delete-orphan")

class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=True, index=True)
    content = Column(String, nullable=True, index=True)
    category = Column(String, nullable=True, index=True)
    published = Column(Boolean, nullable=True, server_default='True')
    createdAt = Column(TIMESTAMP(timezone=True), nullable=True, server_default=func.now())
    updatedAt = Column(TIMESTAMP(timezone=True), default=None, onupdate=func.now())
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="notes")


class APIKey(Base):
    __tablename__ = 'api_keys'
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, nullable=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="api_keys")

