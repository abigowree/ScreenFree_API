from pydantic import BaseModel
from datetime import datetime

class ReportCreate(BaseModel):
    user_id: int
    screen_time_before: int
    screen_time_after: int
    report_date: datetime
    improvement_percent: float

class ReportResponse(ReportCreate):
    report_id: int

    class Config:
        orm_mode = True
