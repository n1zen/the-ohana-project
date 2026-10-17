# FastAPI backend

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scalar_fastapi import get_scalar_api_reference

from database import Base, engine
from lotto_script import get_table_with_api

from routers import (
    dev_routes
)

@asynccontextmanager
async def lifespan(_app: FastAPI):
    # Startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Shutdown
    await engine.dispose()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dev_routes.router, prefix="/api/dev_routes", tags=["dev_routes"])

@app.get("/", include_in_schema=False)
async def home():
    return "Hello, Welcome to the Ohana Project"

@app.get("/lotto")
async def test_lotto_script():
    return await get_table_with_api(game_name="all", start_date="October 15, 2026", end_date="October 15, 2026")

@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        title="The Ohana Project",
        openapi_url=app.openapi_url
    )
