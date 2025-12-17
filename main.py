
from fastapi import FastAPI
from db.database import Base, engine
from routers import activities,reports,schedule,self_assesment,users

 

app = FastAPI(title="Screen Free API")

Base.metadata.create_all(bind=engine)

app.include_router(activities.router)
app.include_router(reports.router)
app.include_router(schedule.router)
app.include_router(self_assesment.router)
app.include_router(users.router)



