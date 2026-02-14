#Завдання 1

from datetime import datetime
def get_days_from_today(date: str) -> int: | ValueError:
    """The function calculates the number of days between a date and the current date
    Args: 
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

 



def add_one(number):

    return number +1
    add_one(5)

print(add_one)
 

x = "Olha,"
y = len(x)
print("Hello, " + x + " how are you?")
print(y)



menu = ["wraps", "sandwiches", "soup", "salad"]
print("Our menu:")
for item in menu:
    print(item)



food = ["1", "2", "3"]
print("select food:")
for number in food:
    print(number)


user_profile = {"name": "Wendy", "status": "active"}
print("\nUser data:")
for key in user_profile:
    print(f"{key}: {user_profile[key]}")


person = {"name": "Olha", "age": 30, "city": "Kyiv"}
print("User data:")
for x in person:
    print(f"{x}: {person[x]}") 

def greet():
    return "Hello,"
print("\n", greet(), "stranger")

age = int(input("\nСкільки тобі років? "))
if age >=99:
    print("Схоже, ти з іншої планети")
else:           
    print("\nв наступному році тобі виповниться:", age + 1)

person = {"name": "Olha", "age": 30, "city": "Kyiv"}
print("\n" + "User data:")
for x in person:
    print(f"{x}: {person[x]}") 

my_lucky_number = 7
guess = int(input("Введи щасливий номер: "))
while my_lucky_number != guess:
    guess = int(input("Упс, не вгадав, введи інший номер: "))
print("Поздоровляємо!")
