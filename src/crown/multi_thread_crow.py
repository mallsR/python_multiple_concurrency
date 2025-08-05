import blog_spider
import time
from loguru import logger
import threading

def single_thread():
    for url in blog_spider.urls:
        blog_spider.crow(url)

def multi_thread():
    # 声明线程
    threads = []
    for url in blog_spider.urls:
        threads.append(
            threading.Thread(
                target=blog_spider.crow,
                args=(url,)
            )
        )

    # 启动线程
    for thread in threads:
        thread.start()

    # 等待线程结束
    for thread in threads:
        thread.join()

if __name__  == '__main__':
    logger.info("开始进行单线程爬虫...")
    begin_time = time.time()
    single_thread()
    logger.info(f"single_thread耗时: {time.time() - begin_time}")

    logger.info("开始进行多线程爬虫...")
    begin_time = time.time()
    multi_thread()
    logger.info(f"multi_thread耗时: {time.time() - begin_time}")
