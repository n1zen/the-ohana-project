# routes/endpoints for dev toollss

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from lotto_script import get_table_with_api

router = APIRouter()

# (dev only) test 
@router.get("/test")
async def dev_test():
    return "Hello world"

@router.get("/scrape-lotto")
async def scrape_lotto():
    game_name = "all"
    start_date = "October 15, 2026"
    end_date = "October 15, 2026"

    return await get_table_with_api(game_name=game_name, start_date=start_date, end_date=end_date)
