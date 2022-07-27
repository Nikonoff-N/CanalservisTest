import xml.etree.ElementTree as ET
import requests
from datetime import datetime


def getUSDtoRUB()->float:
    #Получаем по АПИ файл и получаем валюту с нужным номером, возвращаем значение
    response = requests.get("https://www.cbr.ru/scripts/XML_daily.asp?date_req=" +datetime.now().strftime('%d/%m/%Y'))
    root = ET.fromstring(response.content)
    for child in root.findall('Valute'):
        if child.attrib['ID'] == "R01235":
            return float(child[4].text.replace(",","."))
 

if __name__ == "__main__":
    print(getUSDtoRUB())