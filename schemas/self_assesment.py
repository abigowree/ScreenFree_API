from pydantic import BaseModel
from datetime import datetime

class SelfAssessmentCreate(BaseModel):
    user_id: int
    score: int
    addiction_level: str
    test_date: datetime

class SelfAssessmentResponse(SelfAssessmentCreate):
    test_id: int

    class Config:
        orm_mode = True
