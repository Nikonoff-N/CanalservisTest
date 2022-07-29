from typing import Optional
import sqlalchemy

from sqlmodel import Field, Session, SQLModel, create_engine,select
from datetime import datetime
from utils import OrderData
import logging

#Модуль для работы с БД

class Order(SQLModel, table=True):
    """Схема заказа для хранения в ДБ
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    order: int
    dollar: float
    date: str
    rub: float

def select_all_orders():
    """Функция для теста функцинала
    """
    with Session(engine) as session:
        statement = select(Order)
        results = session.exec(statement)
        for order in results:
            print(order)


def write_data(data:OrderData):
    """Функция для записи или изменения заказа в ДБ

    Args:
        data (OrderData): Данные о заказе
    """
    with Session(engine) as session:
        statement = select(Order).where(Order.order == data.order)
        try:
            target = session.exec(statement).one()
            #Ищем заказ в таблице
        except:
            #НЕ нашли - добавляем как новый
            logging.info(f'Order {data.order} doesnt exist, adding')
            write_new_data(data,session)
        else:
            #нашли - добавляем исправленную информацию
            logging.info(f'Order {data.order} exists, updating')
            update_data(target,data,session)





def write_new_data(data:OrderData,session:Session):
    """пишем информацию в БД, так как эта функция лишь продолжение предыдущей её не нужна отдельная сессия

    Args:
        data (OrderData): Данные о заказе
        session (Session): Сессия работы с БД
    """
    o = Order(order = data.order,dollar=data.dollar,date = data.date, rub = data.rub)
    session.add(o)
    session.commit()

def update_data(Update:Order,data:OrderData,session:Session):
    """обновляем информацию в БД, так как эта функция лишь продолжение предыдущей её не нужна отдельная сессия

    Args:
        Update (Order): Обновляемый заказ
        data (OrderData): Данные о заказе
        session (Session): Сессия работы с БД
    """

    Update.dollar = data.dollar
    Update.date = data.date
    Update.rub = data.rub
    session.add(Update)
    session.commit()


#Присоединяемся к базе, создаём таблицы
#Здесь используется локальная база данных,что скорее всего будет проблемой в образе Docker
#Для корректной работы скрипта замените строку для подключения к ДБ
engine = create_engine("postgresql://testuser:testuser@localhost:5432/testdb")
SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    with Session(engine) as session:
        select_all_orders()