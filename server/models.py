from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class IotData:
    device_id: Optional[str]
    bldg_name: Optional[str]
    room_name: Optional[str]
    temp: Optional[float]
    humd: Optional[float]
    created_at: datetime = datetime.now()
