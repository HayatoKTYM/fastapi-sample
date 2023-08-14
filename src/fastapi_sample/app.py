import os

from fastapi import FastAPI, HTTPException
from starlette.responses import FileResponse

from .api.dashboard.router import router as dashboard_router
from .api.router import router

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_PATH = os.path.join(BASE_DIR, "build", "index.html")

app = FastAPI()
PREFIX = "/services"
app.include_router(
    dashboard_router, prefix=f"{PREFIX}/api/v1/dashboard", tags=["dashboard"]
)
app.include_router(router, prefix=PREFIX, tags=["user"])


@app.get(f"{PREFIX}")
def root():
    if not os.path.exists(INDEX_PATH):
        raise HTTPException(status_code=404, detail="Index file not found")
    return FileResponse(INDEX_PATH)
