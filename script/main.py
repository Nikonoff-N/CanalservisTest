from googleSheetReader import readData
from dbWorker import write_data
from CB import getUSDtoRUB
from datetime import datetime
from time import sleep
from utils import OrderData
from telega import send_telegram
import logging
# Главный модуль для контроля над всем остальными модулями

messaged_today = []
last_messaged = datetime(2020,9,9)

def main()->None:
    """Оснавная функция, настраиваем логи и исполняем функционал скрипта
    """
    global last_messaged,messaged_today
    message = ""
    logging.basicConfig(filename='log.log', level=logging.INFO,format='%(asctime)s %(levelname)-8s %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('Started')
    data = readData() # получаем данные из таблицы
    current_rub = getUSDtoRUB() #получаем валюту
    today = datetime.today()
    # ПРоверяем прошел ли день с того момента как мы писали
    if (today - last_messaged).days > 0:
        last_messaged = today
        messaged_today = []
    for d in data:
        order = OrderData(int(d[1]),int(d[2]),d[3],int(d[2])*current_rub)
        #Смотрим, не просрочен ли заказ
        if (today - datetime.strptime(d[3],'%d.%m.%Y')).days>0:
            #Смотрим писали ли мы о нём сегодня
            if d[1] not in messaged_today:
                message+=d[1]+"\n"
                messaged_today.append(d[1])
        write_data(order) # Отправляем на запись в БД
    # Если есть о чём писать
    if message:
        send_telegram(f"Просроченны следующие заказы:\n"+message)
    logging.info('Finished')

def setup_worker(interval = 10)->None:
    """Функция для запуска скрипта по интерфалу. Да, не оптимально, есть лучшие варианты

    Args:
        interval (int, optional): Интервал запуска скрипта. Defaults to 10.
    """
    while True:
        main()
        sleep(interval)
if __name__ == '__main__':
    setup_worker(interval=120)