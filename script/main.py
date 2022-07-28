from googleSheetReader import readData
from dbWorker import write_data
from CB import getUSDtoRUB
from datetime import datetime
from time import sleep
from utils import OrderData
import logging
# Главный модуль для контроля над всем остальными модулями

def main()->None:
    """Оснавная функция, настраиваем логи и исполняем функционал скрипта
    """
    logging.basicConfig(filename='log.log', level=logging.INFO,format='%(asctime)s %(levelname)-8s %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('Started')
    data = readData() # получаем данные из таблицы
    current_rub = getUSDtoRUB() #получаем валюту
    data = [OrderData(int(o[1]),int(o[2]),o[3],int(o[2])*current_rub) for o in data] #Упаковываем данные
    for d in data:
        write_data(d) # Отправляем по одноу на запись в БД
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
    setup_worker()