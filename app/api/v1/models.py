import datetime
import enum

from sqlalchemy import (
    Column,
    Enum,
    ForeignKey,
    String,
    Integer,
    DateTime,
    Boolean
)
from app.utils import  generate_uuid
from sqlalchemy.dialects.mssql import JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Event(Base):
    __tablename__ = "events"
    
    id = Column(String(255), default=generate_uuid, primary_key=True, index=True)
    name = Column(String(256), index=True)
    date = Column(DateTime)
    location = Column(String(120))
    available_tickets = Column(Integer)
    map_url = Column(String(355))
    bookings = relationship("Booking", back_populates="event")
    
    

class Booking(Base):
    __tablename__ = "bookings"
    
    id = Column(String(255), default=generate_uuid, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"))
    num_tickets = Column(Integer)
    
    event = relationship("Event", back_populates="bookings")
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns if c!='event'}

