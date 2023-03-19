def write_data(data:list) -> None:
    with open('telephone_directory.txt', 'a', encoding='utf-8') as file:
        for line in data:
            file.write(f'{line} \n')
    print('\nДанные успешно добавлены в справочник\n')

def print_data(data: list) -> None:
    for line in data:
        print(f'>> {line}', end='')
    print('\n')

def search_in_file() -> list:
    search = input('Введите информацию для поиска: ')
    result = list()
    with open('telephone_directory.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if search in line:
                result.append(line)
        if len(result) < 1:
            result.append('Поиск не дал результата, попробуйте изменить параметры поиска.')
        return result
