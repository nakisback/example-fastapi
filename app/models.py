from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import null, text
from .database import Base
from datetime import datetime
from uuid import uuid4

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    owner = relationship("User")



class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    #phone_number = Column(String)

# class User(Base):
#     """
#     The users' auth model
#     """

#     __tablename__ = "users"
#     username: Mapped[str] = Column(primary_key=True, nullable=True)
#     first_name:Mapped[str] = Column(nullable=True)
#     last_name:Mapped[str] = Column(nullable=True)
#     email: Mapped[str] = Column(unique=True, nullable=False)
#     password: Mapped[str] = Column(nullable=False)
#     created_at: Mapped[datetime] = Column(default=datetime.utcnow)
#     verified: Mapped[bool] = Column(default=False)

#     def __str__(self):
#         return f"<User {self.email}>"

class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)
    

