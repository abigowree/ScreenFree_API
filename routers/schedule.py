from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import connect_to_db
from models.schedule import Schedule
from schemas.schedule import ScheduleCreate, ScheduleResponse
from typing import List

router = APIRouter(prefix="/schedule", tags=["Schedule"])

@router.post("/", response_model=ScheduleResponse)
def add_task(task: ScheduleCreate, db: Session = Depends(connect_to_db)):
    new_task = Schedule(**task.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.get("/user/{user_id}", response_model=List[ScheduleResponse])
def user_schedule(user_id: int, db: Session = Depends(connect_to_db)):
    return db.query(Schedule).filter(Schedule.user_id == user_id).all()

@router.put("/{schedule_id}", response_model=ScheduleResponse)
def update_task(
    schedule_id: int,
    data: ScheduleCreate,
    db: Session = Depends(connect_to_db)
):
    task = db.query(Schedule).filter(Schedule.schedule_id == schedule_id).first()
    if not task:
        raise HTTPException(404, "Task not found")

    for key, value in data.dict().items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)
    return task
