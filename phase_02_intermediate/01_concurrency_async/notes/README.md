# Concurrency & Async

## The GIL in 30 seconds
CPython has a Global Interpreter Lock — only **one thread runs Python bytecode at a time**.
- ✅ Use **threading** for I/O-bound work (network, disk) — threads release the GIL during I/O
- ✅ Use **multiprocessing** for CPU-bound work — separate processes, no GIL
- ✅ Use **asyncio** for high-concurrency I/O (thousands of connections)

## asyncio basics
```python
import asyncio

async def fetch(url: str) -> str:
    await asyncio.sleep(1)   # simulates I/O
    return f"data from {url}"

async def main() -> None:
    # Sequential (slow):
    r1 = await fetch("url1")
    r2 = await fetch("url2")

    # Concurrent (fast):
    r1, r2 = await asyncio.gather(fetch("url1"), fetch("url2"))

asyncio.run(main())
```

## Real async HTTP with httpx
```python
import httpx, asyncio

async def fetch_all(urls: list[str]) -> list[str]:
    async with httpx.AsyncClient(timeout=10) as client:
        tasks = [client.get(url) for url in urls]
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        return [r.text for r in responses if isinstance(r, httpx.Response)]
```

## ThreadPoolExecutor (blocking I/O made concurrent)
```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def download(url: str) -> bytes:
    import urllib.request
    with urllib.request.urlopen(url) as r:
        return r.read()

with ThreadPoolExecutor(max_workers=10) as pool:
    futures = {pool.submit(download, url): url for url in urls}
    for future in as_completed(futures):
        data = future.result()
```

## ProcessPoolExecutor (CPU-bound tasks)
```python
from concurrent.futures import ProcessPoolExecutor

def compute(n: int) -> int:
    return sum(i*i for i in range(n))

with ProcessPoolExecutor() as pool:
    results = list(pool.map(compute, [10**6, 10**6, 10**6]))
```

## asyncio Queue (producer/consumer pattern)
```python
async def producer(queue: asyncio.Queue) -> None:
    for i in range(10):
        await queue.put(i)
    await queue.put(None)   # sentinel

async def consumer(queue: asyncio.Queue) -> None:
    while True:
        item = await queue.get()
        if item is None: break
        print(f"processing {item}")
        queue.task_done()
```
