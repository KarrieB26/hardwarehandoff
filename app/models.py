from sqlalchemy import Column, Integer, String, Float, DateTime, ARRAY, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Technician(Base):
    __tablename__ = "technicians"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    certs = Column(ARRAY(String))  # ['A+', 'Network+']
    tools = Column(ARRAY(String))  # ['Multimeter', 'Oscilloscope']
    avg_resolution_time = Column(Float)  # minutes
    current_queue = Column(Integer, default=0)
    location_lat = Column(Float)
    location_lng = Column(Float)


class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, index=True)
    device_type = Column(String)
    issue_category = Column(String)
    urgency = Column(String)
    est_revenue = Column(Float)
    customer_lat = Column(Float)
    customer_lng = Column(Float)

class Assignment(Base):
    __tablename__ = "assignments"
    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, ForeignKey("tickets.id"))
    tech_id = Column(Integer, ForeignKey("technicians.id"))
    match_score = Column(Float)
