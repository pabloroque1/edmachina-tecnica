from fastapi import FastAPI
from routes import lead, course, degree
from database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

app.include_router(lead.router, prefix="/leads", tags=["leads"])
app.include_router(course.router, prefix="/courses", tags=["courses"])
app.include_router(degree.router, prefix="/degrees", tags=["degrees"])


