''' Задача 5_1.  Сделать игру морской бой'''

from random import randint
def create_sea_dimens(diag):            # Генерация пустого поля
    created_list = [[0 for j in range(diag)] for i in range(diag)]
    return created_list

def print_sea_dimens(any_matrix):        # Вывод поля боя в консоль
    print(f'{" ":4}{0:5}{1:5}{2:5}{3:5}{4:5}')
    print()
    temp_count = 0
    for row in any_matrix:
        print(f'{temp_count}', end = '     ')
        for item in row:
            print(f'{ str(item).center(5," ")}', end = '')
        temp_count += 1
        print()

play_field = create_sea_dimens(5)
print('Игра "Морской бой" с компьютером на поле 5 х 5.')
print('Поле выглядит так (слева и сверху - соответственно номера строк и столбцов)')
print_sea_dimens(play_field)
print()
rand_row = randint(0,4)
rand_col = randint(0,4)
play_field[rand_row][rand_col] = 1
# print_sea_dimens(play_field)      - Для проверки работы условия выигрыша
print('Сейчас компьютер случайным образом разместил однопалубный корабль. Вам нужно его подбить.')
print('Выберите уровень сложности игры: "1" - 9 ходов, "2" - 6 ходов, "3" - 3 хода: ', end = '')
diff_level = int(input())
if diff_level == 1: diff_level = 9
elif diff_level == 2: diff_level = 6
elif diff_level == 3: diff_level = 3
for i in range(1, diff_level + 1):
    print(f'Выстрел № {i}: ')
    shot_row = int(input('Введите номер строки: '))
    shot_col = int(input('Введите номер стобца: '))
    if (shot_row == rand_row) and (shot_col == rand_col):
        play_field[shot_row][shot_col] = 'X'
        print('ВЫ ПОБЕДИЛИ!  Хроника событий: ')
        print_sea_dimens(play_field)
        break
    else:
        if (play_field[shot_row][shot_col] == 0):
            play_field[shot_row][shot_col] = '-'
            print('Промазал..')
        elif (play_field[shot_row][shot_col] == '-'):
            print('Вы уже стреляли в это место. Будьте внимательнее.')
    if (i == diff_level):
        print('Вы проиграли... Хроника событий:')
        print_sea_dimens(play_field)
        break
print('Game over.')