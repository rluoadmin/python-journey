import asyncio


async def work():
    print("start")
    print("work")
    print("end")
    return "Completed"


result = asyncio.run(work())
print(result)
