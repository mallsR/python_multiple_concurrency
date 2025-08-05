from venv import logger

import requests

urls = [
    f"https://www.cnblogs.com/#p{page}"
    for page in range(1, 50 + 1)
]

def crow(url):
    response = requests.get(url)
    logger.info(response.status_code, len(response.text))


crow(urls[0])