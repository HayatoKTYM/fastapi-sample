from fastapi import APIRouter, Form

from .docs import API_DESC

router = APIRouter()


@router.get("/user-info/")
def get_user_info():
    return {"user": "Information about user"}


@router.get("/user/{u_id}", description=API_DESC["get_user"])
async def get_user(u_id: str = None):
    if not u_id:
        return

    q = f"SELECT max_cpu, max_memory FROM results WHERE uid='{u_id}'"
    return {"message": q}


@router.post("/ingest", description=API_DESC["ingest_log"])
async def ingest_log(top: str = Form(...)):
    logs = [log.strip().split() for log in top.split("\n") if log]
    return {"message": logs[0]}
