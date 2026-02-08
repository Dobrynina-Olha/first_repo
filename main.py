#Завдання 1

from datetime import datetime, date as date_class
def get_days_from_today(date_str: str) -> int:
    try:
        given_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        today = date_class.today()
        delta = today - given_date
        return delta.days
    except ValueError:
        return 0
    


#Завдання 2
import random
def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or min > max or quantity > (max - min + 1):
        return []
    numbers = random.sample (range(min, max + 1), quantity)
    return sorted(numbers)

#Завдання 3
import re

def normalize_phone(phone_number):
    digits = re.sub(r"\D", "", phone_number)
    if digits.startswith("38"):
        return digits
    return "38" + digits
print(normalize_phone("067\t123 4567"))
print(normalize_phone("(095) 234-5678"))
print(normalize_phone("+380 44 123 45 67"))
print(normalize_phone("380501234567"))

#Завдання 4
from datetime import datetime, date, timedelta

def get_upcoming_birthdays(users):
    today = date.today()
    end_date = today + timedelta(days=7)
    result = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if today <= birthday_this_year <= end_date:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            result.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return result
users = [
    {"name": "Neta Velychko", "birthday": "1985.01.23"},
    {"name": "Lena Demina", "birthday": "1990.01.27"},
    {"name": "Volodymyr Poroshenko", "birthday": "1992.02.10"}
]

print(get_upcoming_birthdays(users))



