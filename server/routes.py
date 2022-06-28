from datetime import datetime
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.models import IotDataSchema

router = APIRouter()

iotdata = {
    "1": {
        "device_id": "esp_01",
        "bldg_name": 'techbldg',
        "room_name": 'rm01',
        'temp': 23.4,
        'humd': 76.4,
        'created_at': datetime.now()
    },
    "2": {
        "device_id": "esp_01",
        "bldg_name": 'techbldg',
        "room_name": 'rm01',
        'temp': 34.1,
        'humd': 68.2,
        'created_at': datetime.now()
    },
}

@router.get('/')
async def get_iot_data() -> dict:
    return {
        'data': iotdata
    }

@router.get('/{did}')
async def get_data(did: str) -> dict:
    # if int(id) > len(iotdata):
    #     return {
    #         'error': 'Invalid data id'
    #     }

    for d in iotdata.keys():
        if d == did:
            return {
                'data': iotdata[d]
            }