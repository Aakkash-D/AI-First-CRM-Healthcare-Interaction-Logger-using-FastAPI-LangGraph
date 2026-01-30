
from sqlalchemy import Column, Integer, String, Text, Date, Time, ForeignKey
from database import Base

class HCP(Base):
    __tablename__ = "hcp"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

class Interaction(Base):
    __tablename__ = "interaction"
    id = Column(Integer, primary_key=True)
    hcp_name = Column(String)
    interaction_type = Column(String)
    date = Column(Date)
    time = Column(Time)
    topics = Column(Text)
    sentiment = Column(String)
    materials = Column(Text)
    outcomes = Column(Text)
    follow_up = Column(Text)
