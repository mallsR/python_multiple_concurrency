from venv import logger

import requests

urls = [
    f"https://www.cnblogs.com/#p{page}"
    for page in range(1, 50 + 1)
]

def crow(url):
    """
    爬取资源
    :param url:
    :return:
    """
    response = requests.get(url)
    logger.info(response.status_code, len(response.text))
    return response.text

def parse(html):
    '''
    解析资源: 自定义解析资源的操作
    :param html:
    :return:
    '''
    pass


crow(urls[0])