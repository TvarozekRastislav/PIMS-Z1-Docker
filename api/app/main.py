from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import crud_handler
import math

app = FastAPI()


@app.get("/")
def all_records():
    data = crud_handler.get_all()
    if data.empty:
        raise HTTPException(status_code=404, detail="No data")
    return data.to_dict(orient="records")


@app.get("/{throw_id}")
def id_record(throw_id: str):
    data = crud_handler.get_throw_id(throw_id)
    if data.empty:
        raise HTTPException(status_code=404, detail="No record with given id")
    return data.to_dict(orient="records")


@app.delete("/{throw_id}")
def remove_thorw(throw_id: str):
    data = crud_handler.remove_throw(throw_id)
    return data.to_dict(orient="records")


@app.post("/")
async def root(request: Request):
    G = 9.81
    TS = 0.01
    fall_data = []

    try:
        request = await request.json()
        speed = request["speed"]
        angle = request["angle"]

        if speed < 0 or angle < 0:
            raise HTTPException(status_code=400, detail="Input cannot be negative")

    except Exception as e:
        raise HTTPException(status_code=400, detail="Wrong input")

    x, y, t = 0.0, 0.0, 0.0
    ANGLE_RAD = math.radians(angle)
    FALL_TIME = (2 * speed * math.sin(ANGLE_RAD)) / G

    fall_data.append({"t": 0.0, "x": 0.0, "y": 0.0})

    while t < FALL_TIME:
        t += TS
        x = speed * t * math.cos(ANGLE_RAD)
        y = speed * t * math.sin(ANGLE_RAD) - (G * math.pow(t, 2) / 2.0)

        if t > FALL_TIME:
            x = (math.pow(speed, 2) * math.sin(2.0 * ANGLE_RAD)) / G
            fall_data.append({"x": x, "y": 0.0, "t": FALL_TIME})

            return JSONResponse(crud_handler.insert_calc(fall_data))

        fall_data.append({"x": x, "y": y, "t": t})

    raise RuntimeError("ERROR: Logical error")
