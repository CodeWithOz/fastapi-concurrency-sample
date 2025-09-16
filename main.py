import asyncio
from time import sleep
from fastapi import FastAPI
from fastapi.background import BackgroundTasks
from fastapi.concurrency import run_in_threadpool
import logging


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI()


def upload_to_s3():
    # assume the upload will run synchronously for 5 seconds
    logger.info("Before sleep")
    sleep(5)
    # await asyncio.sleep(5)
    logger.info("After sleep")


@app.get("/process-files")
async def process_files(background_tasks: BackgroundTasks):
    logger.info("Before process files")
    background_tasks.add_task(run_in_threadpool, upload_to_s3)
    logger.info("After process files")
    return {"ok": True}
