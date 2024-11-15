from datetime import datetime

try:
    moscowTimes = datetime.strptime("Wednesday, October 2, 2002", "%A, %B %d, %Y")
    print(moscowTimes)
except ValueError:
    print("ошибка: дата и шаблон даты не совпадают")

try:
    guardian = datetime.strptime("Friday, 11.10.13", "%A, %d.%m.%y")
    print(guardian)
except ValueError:
    print("ошибка: дата и шаблон даты не совпадают")

try:
    dailyNews = datetime.strptime("Thursday1, 18 August 1977", "%Y, %d %B %Y")
    print(dailyNews)
except:
    print("ошибка: дата и шаблон даты не совпадают")