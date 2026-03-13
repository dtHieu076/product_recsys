from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from ....database import get_db
from ....entities.user import User
from ....dtos.user_request import UserLoginRequest
from ....dtos.token_response import TokenResponse
from ....core.security import verify_password, create_access_token, settings
from sqlalchemy import select
from datetime import timedelta

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=TokenResponse)
async def login(form_data: UserLoginRequest, db: AsyncSession = Depends(get_db)):
    # Query user
    stmt = select(User).where(User.username == form_data.username)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()
    
    if not user or form_data.password != user.password:  # Update to bcrypt later
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.user_id)}, expires_delta=access_token_expires
    )
    return TokenResponse(access_token=access_token, token_type="bearer")

