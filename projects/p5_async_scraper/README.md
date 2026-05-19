# Async Web Scraper at Scale

## Goal
Scrape 10,000+ pages concurrently using asyncio + httpx or playwright. Respect robots.txt, implement rate limiting, deduplicate URLs, store to Parquet. Profile memory and throughput with memray.

**Key skills:** asyncio, httpx, playwright, asyncio.Queue, memray, Parquet

## Structure
```
p5_async_scraper/
├── starter/    ← skeleton code with TODOs
└── solution/   ← complete reference implementation
```

## Setup
```bash
cd p5_async_scraper/starter
pip install -r requirements.txt
```

## How to work on it
1. Read this README fully
2. Start with `starter/` — fill in the TODOs in order
3. Run tests along the way: `pytest starter/`
4. When done (or stuck), compare with `solution/`
