import time
import asyncio


# SYNCHRONOUS — total time: 9 seconds (3+3+3, sequential)
def call_llm(prompt: str) -> str:
    time.sleep(3)  # simulates LLM API latency
    return f"Response to: {prompt}"


def main():
    r1 = call_llm("What is LangChain?")
    r2 = call_llm("What is LangGraph?")
    r3 = call_llm("What is LangSmith?")
    print(r1, r2, r3)


# ASYNC — total time: ~3 seconds (all 3 run concurrently)
async def call_llm_async(prompt: str) -> str:
    await asyncio.sleep(3)  # yields control while waiting
    return f"Response to: {prompt}"


async def main_async():
    r1, r2, r3 = await asyncio.gather(
        call_llm_async("What is LangChain?"),
        call_llm_async("What is LangGraph?"),
        call_llm_async("What is LangSmith?"),
    )
    print(r1, r2, r3)


asyncio.run(main_async())
