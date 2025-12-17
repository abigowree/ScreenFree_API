from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import connect_to_db
from models.users import Users
from schemas.users import UserCreate, UserResponse, UserLogin

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(connect_to_db)):
    new_user = Users(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login")
def login(data: UserLogin, db: Session = Depends(connect_to_db)):
    user = db.query(Users).filter(
        Users.email == data.email,
        Users.password == data.password
    ).first()

    if not user:
        raise HTTPException(401, "Invalid credentials")

    return {"message": "Login successful", "user_id": user.user_id}

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(connect_to_db)):
    user = db.query(Users).filter(Users.user_id == user_id).first()
    if not user:
        raise HTTPException(404, "User not found")
    return user
