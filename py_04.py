from enum import Enum
import sys

## Data
documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

## Code
class Command(Enum):
    UNDEFINED = 0
    QUIT = 1
    NAME = 2
    DIRECTORY = 3

# cmd is main function
def cmd(docs, dirs):
    while True:
        print('Введите команду:')
        match read_command():
            case Command.UNDEFINED:
                print('неизвестная команда\n')
            case Command.QUIT:
                return
            case Command.NAME:
                cmd_name(docs)
            case Command.DIRECTORY:
                cmd_directory(dirs)


# read command from stdin and returns corresponding enum value
def read_command():
    com = sys.stdin.readline().strip()
    match com:
        case 'q':
            return Command.QUIT
        case 'p':
            return Command.NAME
        case 's':
            return Command.DIRECTORY
    return Command.UNDEFINED

# find name by document number
def find_name_by_number(docs, number):
    for doc in docs:
        if doc['number'] == number:
            return doc['name']
    return ''

# find shelf number by document number
def find_directory_by_number(dirs, number):
    for dir, docs in dirs.items():
        for doc_number in docs:
            if doc_number == number:
                return dir
    return 0


# command to find name by number
def cmd_name(docs):
    print('Введите номер документа:')
    number = sys.stdin.readline().strip()
    name = find_name_by_number(docs, number)
    print('Результат:')
    if name == '':
        print('Владелец документа: не найден\n')
    else:
        print(f"Владелец документа: {name}\n")


# command to find shelf number by document numebr
def cmd_directory(dirs):
    print('Введите номер документа:')

    number = sys.stdin.readline().strip()
    dir_number = find_directory_by_number(dirs, number)

    print('Результат:')

    if dir_number == 0:
        print('Полка с документом не найден\n')
    else:
        print(f"Документ хранится на полке: {dir_number}\n")

if __name__ == '__main__':
    cmd(documents, directories)