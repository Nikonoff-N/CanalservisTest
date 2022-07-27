from typing import Optional
import sqlalchemy

from sqlmodel import Field, Session, SQLModel, create_engine,select
from datetime import datetime
from utils import OrderData
import logging
class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    order: int
    dollar: float
    date: str
    rub: float


def select_all_orders():
    with Session(engine) as session:
        statement = select(Order)
        results = session.exec(statement)
        for order in results:
            print(order)

def write_data(data:OrderData):
    with Session(engine) as session:
        statement = select(Order).where(Order.order == data.order)
        try:
            target = session.exec(statement).one()
        except:
            logging.info(f'Order {data.order} doesnt exist, adding')
            write_new_data(data,session)
        else:
            logging.info(f'Order {data.order} exists, updating')
            update_data(target,data,session)





def write_new_data(data:OrderData,session:Session):
    o = Order(order = data.order,dollar=data.dollar,date = data.date, rub = data.rub)
    session.add(o)
    session.commit()

def update_data(Update:Order,data:OrderData,session:Session):
    Update.dollar = data.dollar
    Update.date = data.date
    Update.rub = data.rub
    session.add(Update)
    session.commit()


engine = create_engine("postgresql://testuser:testuser@localhost:5432/testdb")
SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    with Session(engine) as session:
        session.commit()
        select_all_orders()