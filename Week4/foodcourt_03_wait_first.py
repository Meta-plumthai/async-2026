# foodcourt_03_wait_first.py
import asyncio
from time import ctime, time
from turtle import done
from food_utils import send_order_to_kitchen

async def main(): 
    my_student_id = "6720301002"
    print(f"{ctime()} | --- [Task 3] Practice using wait (FirstCompleted) ---")
    start_time = ctime()

    #1 spawn 3 concurrent tasks to order food from different kitchens
    t1 = asyncio.create_task(send_order_to_kitchen(my_student_id, "steak", "Sizzling Steak"))
    t2 = asyncio.create_task(send_order_to_kitchen(my_student_id, "noodle", "Wonton Noodle"))
    t3 = asyncio.create_task(send_order_to_kitchen(my_student_id, "hainanese_chicken", "Chicken Rice Thigh"))

    done, pending = await asyncio.wait([t1, t2, t3], return_when=asyncio.FIRST_COMPLETED)
    
    fastest_task = list(done)[0].result()
    print(f"{ctime()} | Winner served dish: Shop: {fastest_task['shop']} | Menu: {fastest_task['menu']}")

    print(f"{ctime()} | Cleaning up: Canceling {len(pending)} remaining pending orders...")
    for t in pending:
        t.cancel()
    print(f"{ctime()} | Total waiting time for the first dish: {time() - start_time:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())