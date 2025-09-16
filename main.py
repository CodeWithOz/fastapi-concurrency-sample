from time import sleep
from fastapi import FastAPI
import logging


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI()


async def upload_to_s3():
    # assume the upload will take 5 seconds
    sleep(5)


@app.get("/process-files")
async def process_files():
    logger.info("Before process files")
    await upload_to_s3()
    logger.info("After process files")
