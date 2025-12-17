from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import connect_to_db
from models.reports import Reports
from schemas.reports import ReportCreate, ReportResponse
from typing import List

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.post("/", response_model=ReportResponse)
def create_report(report: ReportCreate, db: Session = Depends(connect_to_db)):
    new_report = Reports(**report.dict())
    db.add(new_report)
    db.commit()
    db.refresh(new_report)
    return new_report

@router.get("/user/{user_id}", response_model=List[ReportResponse])
def user_reports(user_id: int, db: Session = Depends(connect_to_db)):
    return db.query(Reports).filter(Reports.user_id == user_id).all()

@router.get("/{report_id}", response_model=ReportResponse)
def single_report(report_id: int, db: Session = Depends(connect_to_db)):
    report = db.query(Reports).filter(Reports.report_id == report_id).first()
    if not report:
        raise HTTPException(404, "Report not found")
    return report
