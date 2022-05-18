from fastapi import FastAPI
from .routers import shortner_route
from .database import localsession, Base,engine

app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(shortner_route.router)