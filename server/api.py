from fastapi import FastAPI

from server.routes import router as IotDataRouter

app = FastAPI()

@app.get('/')
async def index():
    return {
        "message": "Welcome to IOT Data Api"
    }

app.include_router(IotDataRouter, prefix='/iotdata')