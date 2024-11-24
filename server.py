from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta
import random


app = FastAPI()

# Configuration for the server's process state
CONFIG = {
    "start-time": datetime.now(),
    "delay-seconds": 5,
    "state": "pending"
}

@app.get("/status")
def get_status():
    # Return the current state of the process
    current_time = datetime.now()
    elapsed_time = (current_time - CONFIG["start-time"]).seconds
    print(elapsed_time)

    # Update state if enough time has passed and it is still pending
    if elapsed_time >= CONFIG["delay-seconds"]:
        if CONFIG["state"] == "pending":
            CONFIG["state"] = random.choice(["completed", "error"])

    return JSONResponse(content={"result": CONFIG["state"]})