from fastapi import FastAPI

from core.database import asycn_database
from routes import routes


app = FastAPI()


@app.on_event('startup')
async def startup():
    await asycn_database.connect()


@app.on_event('shutdown')
async def shutdown():
    await asycn_database.disconnect()

app.include_router(routes)