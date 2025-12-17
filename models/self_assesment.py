from sqlalchemy import Column,String,Integer,DateTime,ForeignKey
from db.database import Base


class Self_assesment(Base):
    __tablename__="self_assesment"
    test_id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey("users.user_id"))
    score=Column(Integer)
    addiction_level=Column(String)
    test_date=Column(DateTime)