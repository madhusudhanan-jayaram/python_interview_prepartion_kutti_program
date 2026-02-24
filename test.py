import asyncio

async def test():
    print("starting.....")
    await asyncio.sleep(1)
    print("finished!")

if __name__ == "__main__":
    asyncio.run(test())