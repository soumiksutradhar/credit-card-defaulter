from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.user_schemas import UserCreate, UserResponse
from app.crud.user_crud import create_user

router = APIRouter()

@router.post("/User", response_model=UserResponse)
async def create_user_endpoint(user: UserCreate, db: AsyncSession = get_db()):

	return await create_user(db, user)
