from fastapi import FastAPI

from src.routers import event_request, event_task

app = FastAPI()


app.include_router(event_request.router)
app.include_router(event_task.router)


@app.get("/")
async def root():
    return {"message": "Welcome to SEP Business !"}
