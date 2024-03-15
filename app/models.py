# from .database import Base
from sqlalchemy.orm import DeclarativeBase, Mapped, relationship, mapped_column
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
import datetime
from sqlalchemy import ForeignKey
class Base(DeclarativeBase):
    type_annotation_map = {
        datetime.datetime: TIMESTAMP(timezone=True)
    }


class Listing(Base):
    __tablename__ = "listings"
    listing_id:Mapped[int] = mapped_column(primary_key=True)
    title:Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    price:Mapped[float] = mapped_column(nullable=False)
    location: Mapped[str] = mapped_column(nullable=False)
    nBathrooms:Mapped[int] = mapped_column()
    nRooms: Mapped[int] = mapped_column(nullable=False)
    date_posted: Mapped[datetime.datetime] = mapped_column(nullable=False, server_default=text('now()'))
    images:Mapped[str] = mapped_column(nullable=True)
    status: Mapped[str] = mapped_column(nullable=False)
    type: Mapped[str] = mapped_column(default="any")

   


class User(Base):
    __tablename__ = "users"
    id:Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    firstName: Mapped[str] = mapped_column(nullable=False)
    lastName: Mapped[str] = mapped_column(nullable=False)
    created_At: Mapped[datetime.datetime] = mapped_column(nullable=False, server_default=text('now()'))

class Message(Base):
    __tablename__  = "messages"
    message_id:Mapped[int] = mapped_column(primary_key=True)
    sender_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    receiver_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    messageContent: Mapped[str] = mapped_column(nullable=False)
    timestamp:Mapped[datetime.datetime] = mapped_column(nullable=False, server_default=text('now()'))

class Favorite(Base):
    __tablename__ = "favorites"
    favorite_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    listing_id: Mapped[int] = mapped_column(ForeignKey("listings.listing_id", ondelete="CASCADE"), nullable=False)

class Comments(Base):
    __tablename__  = "comments" 
    comment_id: Mapped[int] =  mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    listing_id: Mapped[int] = mapped_column(ForeignKey("listings.listing_id", ondelete="CASCADE"), nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)
    timestamp:Mapped[datetime.datetime] = mapped_column(nullable=False, server_default=text('now()'))


class Report(Base):
    __tablename__ = "reports"
    report_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    listing_id: Mapped[int] = mapped_column(ForeignKey("listings.listing_id", ondelete="CASCADE"), nullable=False)
    report_reason: Mapped[str] = mapped_column(nullable=False)
    timestamp: Mapped[datetime.datetime] = mapped_column(nullable=False, server_default=text('now()'))

