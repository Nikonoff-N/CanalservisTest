from dataclasses import dataclass
# Модуль с вспомогательными типами данных

@dataclass
class OrderData:
    """Тип на подобии struct для передачи данных о заказе между модулями
    """
    order: int
    dollar: float
    date: str
    rub: float
