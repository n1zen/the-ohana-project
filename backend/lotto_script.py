from playwright.async_api import Playwright, async_playwright

def convert_date_string_to_tuple(date_string: str) -> tuple:
    """
    Convert a date string in the format "Month Day, Year" to a tuple (month, day, year).
    Example: "January 4, 2021" -> ("January", "4", "2021")
    """
    month, day_year = date_string.split(" ", 1)
    day, year = day_year.split(", ")
    return month, day, year

async def set_starting_date(page, start_date: str) -> None:
    month, day, year = convert_date_string_to_tuple(start_date)
    await page.locator("#cphContainer_cpContent_ddlStartMonth").select_option(month)
    await page.locator("#cphContainer_cpContent_ddlStartDate").select_option(day)
    await page.locator("#cphContainer_cpContent_ddlStartYear").select_option(year)

async def set_ending_date(page, end_date: str) -> None:
    month, day, year = convert_date_string_to_tuple(end_date)
    await page.locator("#cphContainer_cpContent_ddlEndMonth").select_option(month)
    await page.locator("#cphContainer_cpContent_ddlEndDay").select_option(day)
    await page.locator("#cphContainer_cpContent_ddlEndYear").select_option(year)

async def set_date_range(page, start_date: str, end_date: str) -> None:
    await set_starting_date(page, start_date)
    await set_ending_date(page, end_date)
    
async def set_game_name(page, game_name: str) -> None:
    if game_name.lower() == "all":
        return
    await page.locator("#cphContainer_cpContent_ddlSelectGame").select_option(game_name)

async def get_table_data(page, game_name: str, start_date: str, end_date: str) -> list:
    table_data = []
    await set_game_name(page, game_name)
    await set_date_range(page, start_date, end_date)
    await page.get_by_role("button", name="Search").click()
    rows = await page.get_by_role("row").all()
    for row in rows:
        cells = await row.get_by_role("cell").all_text_contents()
        if cells:  # Only add rows that have data
            table_data.append(cells)
    return table_data


async def run_lotto_api(playwright: Playwright, game_name: str, start_date: str, end_date: str) -> list:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://www.pcso.gov.ph/SearchLottoResult.aspx")

    result = []

    table_data = await get_table_data(page, game_name, start_date, end_date)
    result.append(table_data)

    context.close()
    browser.close()

    return result

async def get_table_with_api(game_name: str, start_date: str, end_date: str) -> list:
    async with async_playwright() as playwright:
        return await run_lotto_api(playwright, game_name, start_date, end_date)


# to run headless use "xvfb-run python lotto_script.py"
