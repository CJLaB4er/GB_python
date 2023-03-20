# Ф-я принимает список значений, и добавляет посточно принятые значения в файл.
def write_data(data: list, param: str = 'a') -> None:  # по умолчанию параметр 'a', будет вызов с параметром 'w'
    with open('telephone_directory.txt', param, encoding='utf-8') as file:
        for line in data:
            file.write(f'{line}\n')
    print('\nДанные успешно добавлены в справочник\n')


# Ф-я принимает список значений и выводит его в консоль в отредактированном виде
def print_data(data: list) -> None:
    for line in data:
        print(f'>> {line}', end='')


# Внутри ф-и вводится параметр по которому происходит поиск внутри справочника, и возвращает список найденых строк.
def search_in_file() -> list:
    search = input('Введите информацию для поиска: ')
    result = list()
    with open('telephone_directory.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if search.lower() in line.lower():
                result.append(line)
        return result


# Ф-я по введенному параметру находит строку(и) и перезаписывает файл без найденных строк
def delete_line_in_file() -> None:
    delete_data = search_in_file()
    print('Следующие строки будут удалены:')
    print_data(delete_data)
    choice = input('Введите Да, для подтверждения, ввод иного значения вернет вас в начало программы ')
    if choice.lower() == 'да':
        data = list()
        with open('telephone_directory.txt', 'r', encoding='utf-8') as file:
            for line in file:
                if line not in delete_data:
                    data.append(line[:-1])
        write_data(data, 'w')

# Ф-я принимает список из одного значения - строку которую надо изменить, и заменяет ее на вновь введённое значение
def change_line_in_file(line: list) -> None:
    print(f'Строка >>{line[0][:-1]}<< будет изменена')
    new_line = input('Введите новое значение')
    data = list()
    with open('telephone_directory.txt', 'r', encoding='utf-8') as file:
        for i in file:
            if i != line[0]:
                data.append(i[:-1])
            else:
                data.append(new_line)
    write_data(data, 'w')
