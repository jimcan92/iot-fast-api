from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server.db import database, iot_data_table
from server.routes import router as IotDataRouter

app = FastAPI()
app.add_middleware(CORSMiddleware)


@app.on_event("startup")
async def database_connect():
    await database.connect()
    query = f'''
    CREATE TABLE IF NOT EXISTS {iot_data_table} (
        id INTEGER PRIMARY KEY UNIQUE,
        device_id TEXT,
        bldg_name TEXT,
        room_name TEXT,
        temp REAL,
        humd REAL,
        created_at TEXT
    )
    '''
    await database.execute(query)

    y = await database.fetch_all(f'SELECT * FROM {iot_data_table}')
    print(y)


@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()


@app.get("/")
async def index():
    return {"message": "Welcome to IOT Data Api"}


app.include_router(IotDataRouter, prefix="/api/v1/iotdata")
