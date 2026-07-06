import asyncio


# --- Coroutine — a function defined with async def ---
# Calling it does NOT run it. It returns a coroutine object.
async def greet(name: str) -> str:
    await asyncio.sleep(1)  # non-blocking wait
    return f"Hello, {name}"


# This just creates the coroutine object — nothing runs yet
coro = greet("Mohsin")
print(coro)  # <coroutine object greet at 0x...>

# To actually run it, you need the event loop
result = asyncio.run(greet("Mohsin"))
print(result)  # Hello, Mohsin


# --- Tasks — schedule a coroutine to run on the event loop ---
# Tasks run concurrently. create_task starts it immediately.
async def main():
    # Without tasks — sequential despite being async
    r1 = await greet("LangChain")  # waits 1s
    r2 = await greet("LangGraph")  # then waits 1s
    # Total: 2 seconds

    # With tasks — concurrent
    t1 = asyncio.create_task(greet("LangChain"))  # starts NOW
    t2 = asyncio.create_task(greet("LangGraph"))  # starts NOW
    r1 = await t1  # wait for t1 to finish
    r2 = await t2  # already done by now
    # Total: ~1 second

    print(r1, r2)


asyncio.run(main())

# --- Key mental model ---
# await = "pause HERE and let other coroutines run while waiting"
# create_task = "schedule this to run concurrently, don't wait yet"
