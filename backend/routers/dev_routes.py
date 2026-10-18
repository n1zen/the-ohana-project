# routes/endpoints for dev toollss

from typing import Annotated
from datetime import date, datetime, timedelta
from decimal import Decimal

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from lotto_script import get_table_with_api
from schemas import LottoResponse

router = APIRouter()

# (dev only) test 
@router.get("/test")
async def dev_test():
    return "Hello world"

# (dev only) test scraper
@router.get("/test/scrape-lotto-latest", response_model=list[LottoResponse])
async def scrape_lotto_latest():
    # get latest lotto draw results
    game_name = "all"
    start_date = get_date_today()
    end_date = get_date_today()
    lotto_results = await get_table_with_api(game_name=game_name, start_date=start_date, end_date=end_date)
    # if there are no draw results today, then get the draw resultss yyestarday
    if not lotto_results:
        start_date = get_date_yesterday()
        end_date = get_date_yesterday()
        lotto_results = await get_table_with_api(game_name=game_name, start_date=start_date, end_date=end_date)
    result = []
    for row in lotto_results:
        result.append(convert_to_dict(row))
    return result

# converts raw lotto draw result to a dictionary
def convert_to_dict(list: list):
    return {
        "game_name": list[0].strip(),
        "combination": list[1].strip(),
        "draw_date": datetime.strptime(list[2].strip(), "%m/%d/%Y"),
        "prize_pool": Decimal(list[3].strip().replace(",", "")),
        "amount_of_winners": int(list[4].strip()),
    }

# get formatted date yesterday
# date format: MONTH day, YEAR (i.g. "October 10, 2026")
def get_date_yesterday() -> str:
    date_yesterday = date.today() - timedelta(days=1)
    return f"{date_yesterday:%B} {date_yesterday.day}, {date_yesterday.year}"

# get formatted date today
# date format: MONTH day, YEAR (i.g. "October 10, 2026")
def get_date_today() -> str:
    date_today = date.today()
    return f"{date_today:%B} {date_today.day}, {date_today.year}"
