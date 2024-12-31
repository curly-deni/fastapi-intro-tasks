from fastapi import FastAPI, Query, HTTPException

app = FastAPI()

# BEGIN (write your solution here)
@app.get("/filter")
async def filter_range(
        min: int = Query(0, ge=0),
        max: int = Query(100, le=100)
):
    if min > max:
        raise HTTPException(status_code=422, detail="min cannot be greater than max")

    return {"min": min, "max": max}
# END
