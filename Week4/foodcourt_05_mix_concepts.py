# foodcourt_05_mix_concepts.py
import asyncio
from time import ctime, time
from food_utils import send_order_to_kitchen

async def main():
    my_student_id = "6720301002"
    print(f"{ctime()} | --- [Task 5] Advanced Practice: Mixing concepts together ---")
    start_time = time()

    noodle_task = asyncio.create_task(send_order_to_kitchen(my_student_id, "noodle", "Egg Noodle"))
    chicken_task = asyncio.create_task(asyncio.wait_for(
        send_order_to_kitchen(my_student_id, "hainanese_chicken", "Chicken Rice Special"), 
        timeout=1.0
    ))
    try:
        result = await asyncio.gather(noodle_task, chicken_task)
        print(f"{ctime()} | Success: All food served on time! Received {len(result)} dishes.")
    except asyncio.TimeoutError:
        print(f"{ctime()} | Error: An unexpected timeout occurred during order processing.")

    print(f"{ctime()} | Total elapsedtime: {time() - start_time:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())