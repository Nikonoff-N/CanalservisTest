from dataclasses import dataclass

@dataclass
class OrderData:
    order: int
    dollar: float
    date: str
    rub: float
