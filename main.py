# from fastapi import FastAPI
# from db.database import Base,engine

# from routers.users import user_router
# from routers.activities import activity_router
# from routers.reports import report_router
# from routers.schedule import schedule_router
# from routers.self_assesment import assessment_router


# Base.metadata.create_all(bind=engine)
# app=FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello":"World"}


# app.include_router(user_router)
# app.include_router(activity_router)
# app.include_router(report_router)
# app.include_router(schedule_router)
# app.include_router(assessment_router)

from fastapi import FastAPI
from db.database import Base, engine
from routers import activities,reports,schedule,self_assesment,users

app = FastAPI()

app = FastAPI(title="Screen Free API")

Base.metadata.create_all(bind=engine)

app.include_router(activities.router)
app.include_router(reports.router)
app.include_router(schedule.router)
app.include_router(self_assesment.router)
app.include_router(users.router)
