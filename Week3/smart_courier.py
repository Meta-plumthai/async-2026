# Delivery System): นักศึกษาต้องเขียน try...except CancelledError ได้ถูกต้อง 
# และใช้ .get_name(), .cancel(), และ .cancelled() ได้
import asyncio
from time import ctime

async def delivery_task(package_id, duration):
    try:
        print(f"{ctime()} Courier started delivering {package_id}...")
        while True:
            await asyncio.sleep(duration)
            return (f"{ctime()}Package '{package_id}' delivered!")
    except asyncio.CancelledError:
        print(f"{ctime()} Delivery Canceled! Returning package to warehouse.")
        

async def main():
    task = asyncio.create_task(delivery_task("P001", 5))
    await asyncio.sleep(2)
    print(f"{ctime()} Checking task 'Express-Courier'. Is it done? {task.done()}")
    print(f"{ctime()} Taking too long! Canceling the task...")
    task.cancel() 
    await asyncio.sleep(0.1) 

    print(f"{ctime()} Final verify: Is task officially canceled? {task.cancelled()}")

asyncio.run(main())