documents = [{
    "type": "passport",
    "number": "2207 876234",
    "name": "Василий Гупкин"
}, {
    "type": "invoice",
    "number": "11-2",
    "name": "Геннадий Покемонов"
}, {
    "type": "insurance",
    "number": "10006",
    "name": "Аристарх Павлов"
}]

directories = {'1': ['2207 876234', '11-2'], '2': ['10006'], '3': []}


def people():
    number = input('Номер\n')
    print(f'{search_name(documents, number)}')


def shelf():
    number = input('Номер\n')
    print(f'{search_shelf(directories, number)}')


def show_list():
    print(show_documents(documents))


def add():
    document_type = input('Тип\n')
    number = input('Номер\n')
    name = input('Имя\n')
    shelf = input('Полка\n')
    print(add_element(directories, documents, document_type, number, name, shelf))


def d():
    number = input('Номер\n')
    print(delete(directories, documents, number))


def m():
    number = input('Номер\n')
    shelf = input('Полка\n')
    print(move(directories, number, shelf))


def adds():
    shelf = input('Полка\n')
    print(add_shelf(directories, shelf))


commands = {
        'p': 'people',
        's': 'shelf',
        'l': 'show_list',
        'a': 'add',
        'd': 'd',
        'm': 'm',
        'as': 'adds',
    }


def search_name(documents, number):
    for element in documents:
        if element['number'] == number:
            return element['name']


def search_shelf(directories, number):
    for element in directories:
        if number in directories[element]:
            return element


def show_documents(documents):
    result = ''
    for element in documents:
        result += (
            f'{list(element.values())[0]} "{list(element.values())[1]}" "{list(element.values())[2]}"\n'
        )
    return result


def show_shelf(directories):
    return directories


def add_element(directories, documents, document_type, number, name, shelf):
    if shelf in directories:
        documents.append({'type': document_type, 'number': number, 'name': name})
        directories[shelf].append(number)
        return 'Успешно'
    else:
        return 'Такой полки нет'


def add_shelf(directories, shelf):
    if shelf in directories:
        return 'Такая полка уже есть'
    else:
        directories[shelf] = []
        return 'Успешно'


def delete(directories, documents, number):
    i = True
    for value in documents:
        if number in list(value.values()):
            documents.remove(value)
            i = False

    for value in directories:
        if number in directories[value]:
            directories[value].remove(number)
            i = False
    if i:
        return 'Номер не найден'
    else:
        return 'Успешно'


def move(directories, number, shelf):
    if search_shelf(directories, number) is None:
        return 'Такого номера нет'
    elif shelf not in directories:
        return 'Такой полки нет'
    else:
        for value in directories:
            if number in directories[value]:
                directories[value].remove(number)
        directories[shelf].append(number)
        return 'Успешно'


if __name__ == '__main__':
    while True:
        user_input = input('Введите команду - ')
        if user_input == 'q':
            break
        else:
            command = commands.get(user_input, False)
            if command:
                locals()[command]()
            else:
                print('Неправильная команда')


