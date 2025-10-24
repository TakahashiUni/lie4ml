from fastapi import APIRouter
from ..schemas.users import User

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=list[User])
def get_users():
    return [
        {"id": 1, "name": "TakahashiUnitary", "email": "takahashi.unitary@example.com"}
    ]
