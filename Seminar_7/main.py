import methods

while True:
    print(f'Выберите одно из возможных действий программы:\n'
          f'1 - добавить данные в конец файла\n'
          f'2 - вывести все данные из файла\n'
          f'3 - поиск данных в файле по строкам\n'
          # f'4 - удаление строки\n'
          # f'5 - редактирование строки\n'
          f'5 - выход из программы\n')
    choice = int(input('Введите номер действия: '))
    print()
    match choice:
        case 1:
            methods.write_data()
        case 2: # Здесь будет ссылка на метод вывода всего справочника
            with open('telephone_directory.txt', 'r', encoding='utf-8') as file:
                data = file.readlines()
                methods.print_data(data)
        case 3:
            methods.print_data(methods.search_in_file())
        case 4: # Здесь будет ссылка на метод удаления строк
            pass
        case 5: # Здесь будет ссылка на метод редактировния строки
            pass
        case 5:
            break