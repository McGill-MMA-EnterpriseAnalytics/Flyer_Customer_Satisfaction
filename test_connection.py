from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/endpoint")
async def endpoint(request: Request):
    data = await request.json()
    return {"message": "JSON object received"}