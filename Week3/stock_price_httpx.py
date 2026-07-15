import asyncio
import httpx
from time import ctime


async def fetch_stock_price(server_name: str):
    url = f"http://127.0.0.1:8080/price/{server_name}"
    
    # ใช้ httpx.AsyncClient() ดึงข้อมูลแบบไม่บล็อก Event Loop
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()
        return f"[{data['server']}] Price: {data['price_usd']} USD"


async def main():
    tasks = {
        asyncio.create_task(fetch_stock_price("Alpha"), name="Alpha"),
        asyncio.create_task(fetch_stock_price("Beta"), name="Beta"),
        asyncio.create_task(fetch_stock_price("Gamma"), name="Gamma"),
    }

    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    winner_task = next(iter(done))
    print(f"{ctime()} Winner Result: {winner_task.result()}")

    print(f"{ctime()} Cleaning up {len(pending)} pending tasks...")
    for ongoing_task in pending:
        ongoing_task.cancel()

    await asyncio.gather(*pending, return_exceptions=True)


if __name__ == "__main__":
    asyncio.run(main())