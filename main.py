from __future__ import annotations
from datetime import datetime, date, timedelta
import random
import re

def get_days_from_today(date_str: str) -> int:

"""
Повертає кількість днів від заданої дати (YYYY-MM-DD) до сьогодні.
Якщо дата в майбутньому — буде від'ємне число. 
Якщо формат неправильний — 
піднімає ValueError з зрозумілим повідомленням.
"""

try:
    given_date = datetime.strptime(date_str, "%Y-%m-%d").date()
except (TypeError, ValueError) as e:
    raise ValueError("date має бути рядком у форматі 'YYYY-MM-DD'") from e

today = date.today()
delta = today - given_date
return delta.days

print(get_days_from_today("2020-10-09"))
print(get_days_from_today("2030-01-01"))



