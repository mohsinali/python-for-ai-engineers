import asyncio

# Simulates: Document Loader → Embedder → Vector Store
# Each stage runs independently, passing work via queues


async def document_loader(queue: asyncio.Queue, docs: list[str]):
    """Stage 1: Load documents and put them on the queue."""
    for doc in docs:
        await asyncio.sleep(0.2)  # simulate reading from disk
        await queue.put(doc)
        print(f"[LOADER] Queued: {doc[:30]}...")
    await queue.put(None)  # sentinel value — signals we're done


async def embedder(in_queue: asyncio.Queue, out_queue: asyncio.Queue):
    """Stage 2: Pull docs, embed them, pass forward."""
    while True:
        doc = await in_queue.get()
        if doc is None:  # sentinel received — shut down
            await out_queue.put(None)
            break
        await asyncio.sleep(0.5)  # simulate embedding API call
        embedding = {"doc": doc, "vector": [0.1, 0.2, 0.3]}
        await out_queue.put(embedding)
        print(f"[EMBEDDER] Embedded: {doc[:30]}...")


async def vector_store_writer(out_queue: asyncio.Queue):
    """Stage 3: Pull embeddings and write to vector store."""
    stored = []
    while True:
        item = await out_queue.get()
        if item is None:
            break
        await asyncio.sleep(0.1)  # simulate DB write
        stored.append(item)
        print(f"[STORE] Saved embedding #{len(stored)}")
    print(f"\n✅ Pipeline complete. Stored {len(stored)} embeddings.")


async def main():
    docs = [
        "LangChain is a framework for building LLM applications.",
        "LangGraph extends LangChain with stateful multi-agent workflows.",
        "LangSmith provides tracing and evaluation for LLM pipelines.",
        "Pydantic v2 powers LangChain's type-safe data contracts.",
    ]

    raw_queue = asyncio.Queue(maxsize=2)  # buffers max 2 items
    embed_queue = asyncio.Queue(maxsize=2)

    # All 3 stages run concurrently
    await asyncio.gather(
        document_loader(raw_queue, docs),
        embedder(raw_queue, embed_queue),
        vector_store_writer(embed_queue),
    )


asyncio.run(main())
