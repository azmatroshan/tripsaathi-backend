from fastapi import FastAPI
from app.api.endpoints import user
from app.database import init_db

app = FastAPI()

# Include routers
app.include_router(user.router)

@app.on_event("startup")
async def startup_event():
    await init_db()

@app.get("/")
async def root():
    return {"message": "Welcome to the TripSaathi API"}