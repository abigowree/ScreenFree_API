from pydantic import BaseModel

class ActivityCreate(BaseModel):
    title: str
    category: str
    description: str

class ActivityResponse(ActivityCreate):
    activity_id: int

    class Config:
        orm_mode = True
