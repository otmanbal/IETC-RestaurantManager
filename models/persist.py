# models/persist.py
import json, datetime
from pathlib import Path
from models.order import TableState, Order, OrderItem

FILE = Path(__file__).with_name("orders.json")

def load_states() -> dict[int, TableState]:
    if not FILE.exists(): return {}
    raw = json.loads(FILE.read_text(encoding="utf‑8"))
    states = {}
    for t in raw:
        order = None
        if t["order"]:
            order = Order(
                entrees  =[OrderItem(**d) for d in t["order"]["entrees"]],
                plats    =[OrderItem(**d) for d in t["order"]["plats"]],
                desserts =[OrderItem(**d) for d in t["order"]["desserts"]],
            )
        states[t["table"]] = TableState(
            table_id=t["table"],
            seats=t["seats"],
            status=t["status"],
            order=order
        )
    return states

def save_state(state: TableState):
    data = load_states()
    data[state.table_id] = state
    # sérialisation → JSON
    out = []
    for s in data.values():
        out.append({
            "table":  s.table_id,
            "seats":  s.seats,
            "status": s.status,
            "order": (None if not s.order else {
                "entrees":  [vars(i) for i in s.order.entrees],
                "plats":    [vars(i) for i in s.order.plats],
                "desserts": [vars(i) for i in s.order.desserts],
            })
        })
    FILE.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf‑8")
