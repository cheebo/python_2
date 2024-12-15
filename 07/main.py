import csv
import re

class Person:
    def __init__(self, name, device_type, browser, sex, age, bill, region):
        self.name = name
        self.device_type = device_type
        self.browser = browser
        self.sex = sex
        self.age = age
        self.bill = bill
        self.region = region

    ## Remove double+ space in a name string, to get response as provided in task
    def getname(self):
        return re.sub(' {2,}', ' ', self.name)

    def getdevicetype(self):
        match self.device_type:
            case "mobile":
                return "мобильного браузера"
            case "desktop":
                return "браузера настолького компьютера"
            case "laptop":
                return "браузера для ноутбука"
            case "tablet":
                return "браузера планшета"

    def __str__(self):
        gender = f"{ 'женского' if self.sex == 'female' else 'мужского' } пола"
        action = f"совершил{'а' if self.sex == 'female' else ''}"
        age = f"{ self.age} { 'года' if (int(self.age) % 10) == 1 else 'лет'}"
        return f"Пользователь {self.getname()} {gender}, {age} {action} покупку на {self.bill} у.е. с {self.getdevicetype()} {self.browser}. Регион, из которого совершалась покупка: {self.region}.\n"


def process():
    with open('web_clients_correct.csv', 'r') as file:
        output = open("output.txt", "w")

        reader = csv.reader(file)
        next(reader)  ## Skip the header row
        for row in reader:
            try:
                output.write(str(Person(*row)))
            except Exception as e:
                print(e)

if __name__ == '__main__':
    process()