# routes/endpoints for dev toollss

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db

router = APIRouter()

# (dev only) test 
@router.get("/test")
async def dev_test():
    return "Hello world"
