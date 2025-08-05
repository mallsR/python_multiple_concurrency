import concurrent.futures
import crown.blog_spider as spider

from loguru import logger

if __name__ == '__main__':
    # craw
    with concurrent.futures.ThreadPoolExecutor() as pool:

        htmls = pool.map(spider.crow, spider.urls)
        htmls = list(zip(spider.urls, htmls))
        for url, html in htmls:
            logger.info(f'{url} -> {len(html)}')

        logger.info(f"craw over.")

    # parse
    with concurrent.futures.ThreadPoolExecutor() as pool:
        features = {}
        for url, html in htmls:
            feature = pool.submit(spider.parse, html)
            features[feature] = url

        # 按任务开始顺序,返回执行结果
        for feature, url in features.items():
            logger.info(f'{url} -> {feature.result()}')

        # 依据任务结束顺序,返回执行结果
        for feature in concurrent.futures.as_completed(features):
            logger.info(f'{features[feature]} -> {feature.result()}')