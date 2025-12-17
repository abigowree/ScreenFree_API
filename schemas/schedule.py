from pydantic import BaseModel
from datetime import datetime

class ScheduleCreate(BaseModel):
    user_id: int
    task_name: str
    start_time: datetime
    end_time: datetime
    status: str

class ScheduleResponse(ScheduleCreate):
    schedule_id: int

    class Config:
        orm_mode = True
