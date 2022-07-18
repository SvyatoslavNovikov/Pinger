from pythonping import ping
from datetime import datetime
import time


def myping(host, hostname, loop):
    try:
        ping(host)
        result = (str(loop) + " - " + str(datetime.today()) + ": Есть пинг до " + hostname)
        out(result)
        return 1
    except Exception:
        result = (str(loop) + " - " + str(datetime.today()) + ": Пинг до " + hostname + " отсутствует")
        out(result)
        return 0


def out(result):
    file.write(result + '\n')
    print(result)
    time.sleep(1)


loop = 1

while True:

    if loop == 1:
        file = open("log.txt", "w")
    else:
        file = open("log.txt", "a")

    myping('yandex.ru', "Яндекс DNS", loop)
    myping('77.88.21.11', "Яндекс IP", loop)

    # if myping('yandex.ru', "Яндекс", loop) == 0:
    #     myping('192.168.1.1', 'роутер', loop)

    file.close()
    loop += 1
