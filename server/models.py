from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class IotDataSchema(BaseModel):
    device_id: Optional[str]
    bldg_name: Optional[str]
    room_name: Optional[str]
    temp: Optional[float]
    humd: Optional[float]
    created_at: datetime = datetime.now()

    class Config:
        schema_extra = {
            "example": {
                "title": "ESP Data",
                "content": "ESP Data Monitoring",
            }
        }