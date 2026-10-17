# routes/endpoints for dev toollss

from typing import Annotated
from datetime import date

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

@router.get("/scrape-lotto-today")
async def scrape_lotto_today():
    game_name = "all"
    start_date = get_date_today()
    end_date = get_date_today()
    return await get_table_with_api(game_name=game_name, start_date=start_date, end_date=end_date)

def get_date_today() -> str:
    date_today = date.today()
    return f"{date_today:%B} {date_today.day}, {date_today.year}"
