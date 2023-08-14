from fastapi import APIRouter

router = APIRouter()


@router.get("/recent-logs/")
def get_recent_logs():
    return {"logs": "Recent logs from dashboard"}


@router.get("/monthly-logs/")
def get_monthly_logs():
    return {"logs": "Monthly logs from dashboard"}
