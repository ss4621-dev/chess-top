# main.py

from fastapi import FastAPI
from app.api.endpoints import top_players, players_rating_history, rating_history_csv
from app.db.database import database, metadata


app = FastAPI()

# Include routers
app.include_router(top_players.router)
app.include_router(players_rating_history.router)
app.include_router(rating_history_csv.router)

# Include database initialization
@app.on_event("startup")
async def startup_db():
    await database.connect()

@app.on_event("shutdown")
async def shutdown_db():
    await database.disconnect()
