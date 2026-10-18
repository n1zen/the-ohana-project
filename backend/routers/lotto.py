# routes for LOTTO RESULTS
# mostly only GET requests with filtering and sorting options
# POST requests are only for adding new results to the database (Will be scheduled to run automatically in the future)
from typing import Annotated
from datetime import date, datetime, timedelta
from decimal import Decimal

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

import models
from lotto_dependencies import get_table, lotto_results_exist
from database import get_db
from schemas import LottoResponse

router = APIRouter()

# bulk create lotto results
@router.post("/lotto-scrape-results", response_model=list[LottoResponse], status_code=status.HTTP_201_CREATED)
async def create_lotto_results(
    db: Annotated[AsyncSession, Depends(get_db)],
):
    # get latest lotto draw results
    lotto_results = await get_table()
    # check if lotto results already exist in the database
    await lotto_results_exist(lotto_results, db)
    new_lotto_results_list = []
    for row in lotto_results:
        # create a new Lotto model instance
        new_lotto_result = models.Lotto(
            game_name=row[0].strip(),
            combination=row[1].strip(),
            draw_date=datetime.strptime(row[2].strip(), "%m/%d/%Y"),
            prize_pool=Decimal(row[3].strip().replace(",", "")),
            amount_of_winners=int(row[4].strip()),
        )
        new_lotto_results_list.append(new_lotto_result)
    db.add_all(new_lotto_results_list)
    await db.commit()
    for new_lotto_result in new_lotto_results_list:
        await db.refresh(new_lotto_result)
    return new_lotto_results_list
    
# get all lotto results
@router.get("/lotto-results", response_model=list[LottoResponse])
async def get_lotto_results(
    db: Annotated[AsyncSession, Depends(get_db)]
):
    query = select(models.Lotto)
    result = await db.execute(query)
    return result.scalars().all()

# get lotto results by game name and date range
@router.get("/lotto-results/filter", response_model=list[LottoResponse])
async def get_lotto_results_by_game_and_date_range(
    db: Annotated[AsyncSession, Depends(get_db)],    
    game_name: Annotated[str | None, Query(description="Filter by game name")] = None,
    start_date: Annotated[date, Query(description="Filter by start date (YYYY-MM-DD)")] = None,
    end_date: Annotated[date, Query(description="Filter by end date (YYYY-MM-DD)")] = None,
):
    query = select(models.Lotto)
    if game_name is not None:
        query = query.where(models.Lotto.game_name == game_name)
    if start_date is not None:
        if end_date is not None and start_date > end_date:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Start date cannot be greater than end date",
            )
        query = query.where(models.Lotto.draw_date >= start_date)
    if end_date is not None:
        query = query.where(models.Lotto.draw_date < end_date + timedelta(days=1))
    result = await db.execute(query)
    return result.scalars().all()