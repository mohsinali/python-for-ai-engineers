import asyncio


async def fetch_embedding(text: str, delay: float) -> list[float]:
    await asyncio.sleep(delay)
    # Simulates returning an embedding vector
    return [0.1, 0.2, 0.3]


async def fetch_with_error(text: str) -> list[float]:
    await asyncio.sleep(0.5)
    raise ValueError(f"Embedding API failed for: {text}")


async def main():
    texts = ["What is RAG?", "Define an agent", "Explain LangGraph"]

    # --- gather — runs all concurrently, returns results in ORDER ---
    # Even though delays differ, results match input order
    results = await asyncio.gather(
        fetch_embedding(texts[0], delay=1.0),
        fetch_embedding(texts[1], delay=0.3),
        fetch_embedding(texts[2], delay=0.7),
    )
    print(results)  # 3 embeddings, in original order

    # --- gather with return_exceptions=True ---
    # Without this, ONE failure cancels everything
    # With it, exceptions are returned as values — you handle them
    results = await asyncio.gather(
        fetch_embedding("text 1", delay=0.2),
        fetch_with_error("text 2"),  # this will fail
        fetch_embedding("text 3", delay=0.4),
        return_exceptions=True,
    )

    for text, result in zip(texts, results):
        if isinstance(result, Exception):
            print(f"FAILED — {text}: {result}")
        else:
            print(f"OK — {text}: {result}")


asyncio.run(main())
