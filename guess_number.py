from random import randint
from math import ceil

print('''\n\n Угадай число.\n Устанавите числовой диапазон, a компьютер выберет случайное число, которое вы должны угадать.\n''')

def answer():
    global num
    global range_num
    try:
        num = int(input(" Введите целое число: "))
        if 0 >= num or num > range_num:
            print("\n Число вне диапазона!")
            answer()
    except ValueError:
        print("\n Некорректный ответ!")
        answer()


def range_len():
    global range_num
    try:
        range_num = int(input('\n Введите длину диапазона (целое число): '))
        if 0 >= range_num:
            print("\n Некорректный ответ!")
            range_len()
    except ValueError:
        print("\n Некорректный ответ!")
        range_len()


if __name__=="__main__":
    range_len()

    attempt = ceil(range_num/2)

    unknown_number = randint(1, range_num)
    print(f"\n Попыток: {attempt}")
    for i in range(attempt):
        print(f"\n {i+1}-я поптыка")
        answer()
        if i == attempt-1:
            if num == unknown_number:
                print(f"\n\n Вы угадали число!")
                print("\n\n Игра окончена!")
                break
            else:
                print(f"\n\n Вы не угадали число")
                print("\n\n Игра окончена!")
                break
        if num == unknown_number:
            print(f"\n\n Вы угадали число!")
            print("\n\n Игра окончена!")
            break
        else:
            print("\n Попробуйте еще раз")
