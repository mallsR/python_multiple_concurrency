import threading

from gevent.time import sleep
from loguru import logger

lock = threading.Lock()


class Accont:
    def __init__(self, balance):
        self.balance = balance

def draw(account, amount):
    with lock:
        if account.balance >= amount:
            sleep(0.1)
            account.balance -= amount
            logger.info(f'{threading.current_thread().name} 取钱成功，余额为：{account.balance}')
        else:
            logger.info(f'{threading.current_thread().name} 取钱失败，余额不足')


if __name__ == '__main__':
    account = Accont(1000)
    t1 = threading.Thread(target=draw, args=(account, 800))
    t2 = threading.Thread(target=draw, args=(account, 800))
    t1.start()
    t2.start()