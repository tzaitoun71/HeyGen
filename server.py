from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta
import random


app = FastAPI()

CONFIG = {
    "start-time": datetime.now(),
    "delay-seconds": 20,
    "state": "pending"
}

@app.get("/status")
def get_status():
    current_time = datetime.now()
    elapsed_time = (current_time - CONFIG["start-time"]).seconds
    print(elapsed_time)


    if elapsed_time >= CONFIG["delay-seconds"]:
        if CONFIG["state"] == "pending":
            CONFIG["state"] = random.choice(["completed", "error"])

    return JSONResponse(content={"result": CONFIG["state"]})