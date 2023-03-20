import methods

while True:
    print(f'Выберите одно из возможных действий программы:\n'
          f'1 - добавить данные в конец файла\n'
          f'2 - вывести все данные из файла\n'
          f'3 - поиск данных в файле по строкам\n'
          f'4 - удаление строки\n'
          # f'5 - редактирование строки\n'
          f'6 - выход из программы\n')
    choice = int(input('Введите номер действия: '))
    print()
    match choice:
        case 1:
            data = [input('Введите данные для добавления в справочник: ')]
            # data = ['Первая запись', 'Вторая запись', 'Третья запись']
            methods.write_data(data)
        case 2:
            with open('telephone_directory.txt', 'r', encoding='utf-8') as file:
                data = file.readlines()
                methods.print_data(data)
                print()
        case 3:
            data = methods.search_in_file()
            if len(data) < 1:
                print('\nПо вашему запросу ничего не найдено, повторите попытку.\n')
            else:
                methods.print_data(data)
                print('\n')
        case 4:
            methods.delete_line_in_file()
        case 5: # Здесь будет ссылка на метод редактировния строки
            pass
        case 6:
            break