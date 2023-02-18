def get_matrix():
    print_choose_input_type()
    choose_input_type()


def print_choose_input_type():
    print_horizontal_line()
    print("Выберите тип ввода данных:\n"
          "1. Пользовательский ввод данных\n"
          "2. Ввод данных из файла\n"
          "3. Генерация случайных матриц")


def print_horizontal_line():
    return print("-" * 100)


def choose_input_type():
    input_type_dict = {
        1: user_input_type,
        2: file_input_type,
        3: random_matrix,
    }
    while True:
        input_type = int(input())
        if input_type in input_type_dict.keys():
            input_type_dict[input_type]()
            return print_horizontal_line()
        else:
            print("Неверный ввод данных!")
            print_choose_input_type()


def user_input_type():
    return print("Вы выбрали пользовательский ввод данных, "
                 "но ленивая жопа его ещё не реализовала")


def file_input_type():
    return print("Вы выбрали ввод данных с файла, "
                 "но ленивая жопа его ещё не реализовала")


def random_matrix():
    return print("Вы выбрали генерацию случайных матриц, "
                 "но ленивая жопа его ещё не реализовала")