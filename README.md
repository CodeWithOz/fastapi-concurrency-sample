# FastAPI Background Tasks Demo

This is a simple FastAPI server to work through blocking and non-blocking background tasks. It simulates a blocking upload (e.g., to S3) and shows how FastAPI’s `BackgroundTasks` returns a response immediately while work continues in the background.

## Tech Stack

- FastAPI (standard extras)
- Python 3.13+

## How it works

- [upload_to_s3()](cci:1://file:///Users/ucheozoemena/01-projects/python-async/main.py:16:0-21:30) simulates a blocking operation using `time.sleep(5)`.
- `GET /process-files` enqueues [upload_to_s3](cci:1://file:///Users/ucheozoemena/01-projects/python-async/main.py:16:0-21:30) as a background task via `BackgroundTasks`.
- The endpoint returns immediately, while the blocking function runs in the background.
- Logs illustrate the timing:
  - App: “Before process files” → “After process files”
  - Background task: “Before sleep” → “After sleep”

To experiment with non-blocking behavior, compare `time.sleep(5)` with an async approach (e.g., `await asyncio.sleep(5)`) and adapt the task accordingly.

## Running the app

### Using uv (recommended)
1. Install dependencies:
   - `uv sync`
2. Start the dev server:
   - `uv run fastapi dev main.py`
3. Open the interactive docs:
   - http://127.0.0.1:8000/docs

### Using pip/venv
1. Create and activate a virtual environment:
   - `python -m venv .venv`
   - `source .venv/bin/activate`
2. Install dependencies:
   - `pip install "fastapi[standard]>=0.116.1"`
3. Start the server:
   - `uvicorn main:app --reload`
4. Open the interactive docs:
   - http://127.0.0.1:8000/docs

## Endpoint

- `GET /process-files`
  - Queues a background task that simulates a blocking upload with `time.sleep(5)`.
  - Returns: `{"ok": true}` immediately.

Example:
- `curl http://127.0.0.1:8000/process-files`

## Notes

- The demo code lives in [main.py](cci:7://file:///Users/ucheozoemena/01-projects/python-async/main.py:0:0-0:0), with [upload_to_s3()](cci:1://file:///Users/ucheozoemena/01-projects/python-async/main.py:16:0-21:30) as the blocking task and the `/process-files` route scheduling it in the background.
- Switch `time.sleep(5)` to `await asyncio.sleep(5)` and make the task async if you want to visualize non-blocking behavior end-to-end.