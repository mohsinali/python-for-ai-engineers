import asyncio
import httpx
from contextlib import asynccontextmanager


# --- Async context manager with class ---
class LLMClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client: httpx.AsyncClient | None = None

    async def __aenter__(self):
        # Setup — runs when entering `async with`
        self.client = httpx.AsyncClient(
            headers={"Authorization": f"Bearer {self.api_key}"}, timeout=30.0
        )
        print("Connection opened")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # Teardown — runs when exiting, even if there's an error
        if self.client:
            await self.client.aclose()
        print("Connection closed")
        return False  # don't suppress exceptions

    async def complete(self, prompt: str) -> str:
        # In real code: await self.client.post(...)
        await asyncio.sleep(0.5)
        return f"Completion for: {prompt}"


# --- Async context manager with decorator (simpler) ---
@asynccontextmanager
async def managed_llm_client(api_key: str):
    client = httpx.AsyncClient(
        headers={"Authorization": f"Bearer {api_key}"}, timeout=30.0
    )
    try:
        print("Client ready")
        yield client  # caller gets this value
    finally:
        await client.aclose()
        print("Client cleaned up")


async def main():
    # Class-based
    async with LLMClient(api_key="sk-fake") as llm:
        result = await llm.complete("What is an agent?")
        print(result)

    # Decorator-based
    async with managed_llm_client("sk-fake") as client:
        print(f"Client type: {type(client)}")


asyncio.run(main())
