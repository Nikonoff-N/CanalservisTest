import xml.etree.ElementTree as ET
import requests
from datetime import datetime
#Модуль для получения котировок ЦБ РФ

def getUSDtoRUB()->float:
    """Получаем по АПИ файл и получаем валюту с нужным номером, возвращаем значение

    Returns:
        float: Курс на день запуска скрипта
    """
    response = requests.get("https://www.cbr.ru/scripts/XML_daily.asp?date_req=" +datetime.now().strftime('%d/%m/%Y'))
    root = ET.fromstring(response.content)
    #Ищем ноду по номеру валюты и возвращаем её текст трансформированный в float
    for child in root.findall('Valute'):
        if child.attrib['ID'] == "R01235":
            return float(child[4].text.replace(",","."))
 

if __name__ == "__main__":
    print(getUSDtoRUB())