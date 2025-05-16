# models/order.py
from dataclasses import dataclass, field
from typing import List

@dataclass
class OrderItem:
    name: str
    price: float
    qty: int = 0

    @property
    def total(self): return self.price * self.qty

@dataclass
class Order:
    entrees:   List[OrderItem] = field(default_factory=list)
    plats:     List[OrderItem] = field(default_factory=list)
    desserts:  List[OrderItem] = field(default_factory=list)

    @property
    def total(self):
        return sum(i.total for cat in (self.entrees, self.plats, self.desserts) for i in cat)

@dataclass
class TableState:
    table_id: int
    seats: int
    status: str           # "free" | "occupied"
    order:  Order | None
