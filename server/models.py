from datetime import datetime
from pydantic import BaseModel

class IotDataSchema(BaseModel):
    device_id: str | None
    bldg_name: str | None
    room_name: str | None
    temp: float | int | None
    humd: float | int | None
    created_at: datetime = datetime.now()

    class Config:
        schema_extra = {
            "example": {
                "title": "ESP Data",
                "content": "ESP Data Monitoring",
            }
        }