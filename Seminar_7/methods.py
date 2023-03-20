# Ф-я принимает список значений, и добавляет посточно принятые значения в файл.
def write_data(data: list) -> None:
    with open('telephone_directory.txt', 'a', encoding='utf-8') as file:
        for line in data:
            file.write(f'{line}\n')
    print('\nДанные успешно добавлены в справочник\n')


# Ф-я принимает список значений и выводит его в консоль в отредактированном виде
def print_data(data: list) -> None:
    for line in data:
        print(f'>> {line}', end='')
    print('\n')


# Внутри ф-и вводится параметр по которому происходит поиск внутри справочника, и возвращает список найденых строк.
def search_in_file() -> list:
    search = input('Введите информацию для поиска: ')
    result = list()
    with open('telephone_directory.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if search.lower() in line.lower():
                result.append(line[:-1])  # срез отсекает непечатный символ переноса строки
        if len(result) < 1:
            result.append('Поиск не дал результата, попробуйте изменить параметры поиска.')
        return result


# def delete_line_in_file() -> None:
#     data = search_in_file()
#     write_data(data)
