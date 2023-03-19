def write_data() -> None:
    data = input()
    with open('telephone_directory.txt', 'a', encoding='utf-8') as file:
        file.write(f'{data} \n')
    print('\nДанные успешно добавлены в справочник\n')

def print_data(data: list) -> None:
    for line in data:
        print(f'>> {line}', end='')
    print('\n')