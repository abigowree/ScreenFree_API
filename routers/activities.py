from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import connect_to_db
from models.activities import Activities
from schemas.activities import ActivityCreate, ActivityResponse
from typing import List

router = APIRouter(prefix="/activities", tags=["Activities"])


@router.get("/", response_model=List[ActivityResponse])
def get_activities(db: Session = Depends(connect_to_db)):
    return db.query(Activities).all()

@router.get("/{activity_id}", response_model=ActivityResponse)
def get_activity(activity_id: int, db: Session = Depends(connect_to_db)):
    activity = db.query(Activities).filter(Activities.activity_id == activity_id).first()
    if not activity:
        raise HTTPException(404, "Activity not found")
    return activity
@router.post("/", response_model=ActivityResponse)
def add_activity(activity: ActivityCreate, db: Session = Depends(connect_to_db)):
    new_activity = Activities(**activity.dict())
    db.add(new_activity)
    db.commit()
    db.refresh(new_activity)
    return new_activity

@router.put("/{activity_id}", response_model=ActivityResponse)
def update_activity(
    activity_id: int,
    data: ActivityCreate,
    db: Session = Depends(connect_to_db)
):
    activity = db.query(Activities).filter(Activities.activity_id == activity_id).first()
    if not activity:
        raise HTTPException(404, "Activity not found")

    for key, value in data.dict().items():
        setattr(activity, key, value)

    db.commit()
    db.refresh(activity)
    return activity
