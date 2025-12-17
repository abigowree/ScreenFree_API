from sqlalchemy import Column,Integer,String,DateTime,Float,ForeignKey
from db.database import Base


class Reports(Base):
    __tablename__="reports"
    report_id=Column(Integer, primary_key=True)
    user_id=Column(Integer,ForeignKey("users.user_id"))
    screen_time_before=Column(Integer)
    screen_time_after=Column(Integer)
    report_date=Column(DateTime)
    improvement_percent=Column(Float)

    