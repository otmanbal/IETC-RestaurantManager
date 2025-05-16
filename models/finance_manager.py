import json
from datetime import datetime

FINANCE_FILE = "data/finances.json"

def load_finances():
    try:
        with open(FINANCE_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_finance_entry(entry):
    data = load_finances()
    data.append(entry)
    with open(FINANCE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_financial_record(record_type, description, amount):
    entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "type": record_type,
        "description": description,
        "amount": amount
    }
    save_finance_entry(entry)

def get_financial_summary():
    data = load_finances()
    income = sum(e["amount"] for e in data if e["type"] == "income")
    expense = sum(e["amount"] for e in data if e["type"] == "expense")
    return income, expense, income - expense
