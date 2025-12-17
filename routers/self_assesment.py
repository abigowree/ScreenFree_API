from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import connect_to_db
from models.self_assesment import Self_assesment
from schemas.self_assesment import SelfAssessmentCreate, SelfAssessmentResponse
from typing import List

router = APIRouter(prefix="/self-assessment", tags=["Self Assessment"])

@router.post("/", response_model=SelfAssessmentResponse)
def submit_test(test: SelfAssessmentCreate, db: Session = Depends(connect_to_db)):
    new_test =  Self_assesment(**test.dict())
    db.add(new_test)
    db.commit()
    db.refresh(new_test)
    return new_test

@router.get("/user/{user_id}", response_model=List[SelfAssessmentResponse])
def test_history(user_id: int, db: Session = Depends(connect_to_db)):
    return db.query( Self_assesment).filter(Self_assesment.user_id == user_id).all()

@router.get("/{test_id}", response_model=SelfAssessmentResponse)
def single_test(test_id: int, db: Session = Depends(connect_to_db)):
    test = db.query( Self_assesment).filter( Self_assesment.test_id == test_id).first()
    if not test:
        raise HTTPException(404, "Test not found")
    return test
