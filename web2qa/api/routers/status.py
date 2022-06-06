from fastapi import APIRouter

router = APIRouter(
    prefix="/status",
    tags=["status"],
    responses={404: {"description": "Not found"}},
)

@router.get("/health-check")
async def health_check():
    return {"status": "OK"}
