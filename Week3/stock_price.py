# นักเรียนต้องเลือกใช้ asyncio.wait() พร้อมออปชัน return_when=asyncio.FIRST_COMPLETED เท่านั้น (หากใครใช้ gather หรือ wait_for จะไม่ตรงสเปกเงื่อนไขการแข่งส่งข้อมูล)
import asyncio
from time import ctime

async def fetch_stock_price(server_name, delay):
    await asyncio.sleep(delay)
    return (f"[{server_name}] Price: 150 USD")

async def main():
    tasks = {
        asyncio.create_task(fetch_stock_price("Alpha", 3.0)),
        asyncio.create_task(fetch_stock_price("Beta", 0.8)),
        asyncio.create_task(fetch_stock_price("Gamma", 1.5))
    }
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    for finished_task in done:
        print(f"{ctime()} Fastest Task Result: {finished_task.result()}")
        
    # Clean up the remaining pending tasks to prevent memory leaks
    i = 0
    for ongoing_task in pending:
        ongoing_task.cancel()
        i += 1
    print(f"{ctime()} Cleaning up {i} pending tasks...")       # Expected: 1


asyncio.run(main())