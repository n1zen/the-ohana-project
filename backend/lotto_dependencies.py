# some lotto dependencies that are used for lotto related routes and functions
from datetime import date, timedelta, datetime

from fastapi import HTTPException, status
from sqlalchemy import select, func

import models
from lotto_script import get_table_with_api

async def get_table() -> list:
    # get latest lotto draw results
    game_name = "all"
    start_date = get_date_today()
    end_date = get_date_today()
    lotto_results = await get_table_with_api(game_name=game_name, start_date=start_date, end_date=end_date)
    # if there are no draw results today, then get the draw resultss yestarday
    if not lotto_results:
        start_date = get_date_yesterday()
        end_date = get_date_yesterday()
        lotto_results = await get_table_with_api(game_name=game_name, start_date=start_date, end_date=end_date)
    return lotto_results

# check if lotto result already exists in the database
# throw exception if it does
async def lotto_results_exist(list_of_lotto_results: list, db):
    for row in list_of_lotto_results:
        game_name = row[0].strip()
        combination = row[1].strip()
        draw_date = datetime.strptime(row[2].strip(), "%m/%d/%Y")
        # check if lotto result already exists in the database
        query = select(models.Lotto).where(
            func.lower(models.Lotto.game_name) == game_name.lower(),
            func.lower(models.Lotto.combination) == combination.lower(),
            models.Lotto.draw_date == draw_date
        )
        result = await db.execute(query)
        existing_lotto_result = result.scalar_one_or_none()
        if existing_lotto_result:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Lotto results on {draw_date.strftime('%B %d, %Y')} already exists",
            )

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
