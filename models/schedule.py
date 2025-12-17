from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey
from db.database import Base

class Schedule (Base):
    __tablename__="schedule"
    schedule_id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey("users.user_id"))
    task_name=Column(String)
    start_time=Column(DateTime)
    end_time=Column(DateTime)
    status=Column(String)