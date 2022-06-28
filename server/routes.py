from datetime import datetime
import json
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.models import IotData

from server.db import database, iot_data_table

router = APIRouter()

iotdata = {
    "1": {
        "device_id": "esp_01",
        "bldg_name": "techbldg",
        "room_name": "rm01",
        "temp": 23.4,
        "humd": 76.4,
        "created_at": datetime.now(),
    },
    "2": {
        "device_id": "esp_01",
        "bldg_name": "techbldg",
        "room_name": "rm01",
        "temp": 34.1,
        "humd": 68.2,
        "created_at": datetime.now(),
    },
}


@router.get("/")
async def get_iot_data() -> list[IotData]:
    res = await database.fetch_all(f"SELECT * FROM {iot_data_table}")

    r = [
        IotData(
            d["device_id"],
            d["bldg_name"],
            d["room_name"],
            d["temp"],
            d["humd"],
            d["created_at"],
        )
        for d in res
    ]

    print(r)

    return r


@router.get("/{did}")
async def get_data(did: str) -> dict:
    res = await database.fetch_all(f"SELECT * FROM {iot_data_table} WHERE id={did}")
    return res


@router.post("/")
async def add_data(data: dict):
    query = f"""
    INSERT INTO {iot_data_table} VALUES (
        NULL,
        '{data['device_id']}',
        '{data['bldg_name']}',
        '{data['room_name']}',
        {data['temp']},
        {data['humd']},
        '{datetime.now()}'
    )
    """

    print(query)
    await database.execute(query)
