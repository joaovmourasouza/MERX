from datetime import datetime
import logging

logging.basicConfig(filename=f"logs/{datetime.now().strftime('%Y-%m-%d')}-{datetime.now().strftime('%H-%M-%S')}.log", 
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def info_logging(msg: str) -> None:
    logging.info(msg)

def error_logging(msg: str) -> None:
    logging.error(msg)