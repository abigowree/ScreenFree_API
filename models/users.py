from sqlalchemy import Column ,Integer, String,Boolean, TIMESTAMP
from db.database import Base
from datetime import datetime



class Users(Base):
    __tablename__="users"
    user_id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String)
    password=Column(String)
    role=Column(String)
    created_at=Column(TIMESTAMP,default=datetime.utcnow,nullable=False)