from sqlalchemy import Column,Integer,String,DateTime
from db.database import Base


class Activities(Base):
    __tablename__="activities"
    activity_id = Column(Integer, primary_key=True, index=True)
    title=Column(String)
    category=Column(String)
    description=Column(String)