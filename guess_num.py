"""
Программа генерирует число от 0 до 1_000_000 и предлагает угадать его.

Программа должна приветствовать пользователя и считывать число с клавиатуры
Если число меньше загаданного, то программа выводит сообщение о том, что число
меньше
Если больше загаданного, то программа выводит сообщение о том, что больше

Программа должна выводить сообщения-предупреждения, если:
* пользователь ввёл не число
* число не входит в обозначенный в условии диапазон
Если пользователь ничего не ввёл/ввёл "exit", то происходит выход из программы.

Тебе может понадобится модуль random, цикл while и ветвления
"""

if __name__ == '__main__':
    pass
import random
number = random.randint(0, 1_000_000)
while True:
    answer = input('Угадай число ')
    if not answer or answer == 'exit':
        break
    if not answer.isdigit():
        print('ВВедите число')
    elif int(answer) > 1_000_000:
        print('Введите число до 1000000')
        continue
    if int(answer) > number:
        print('Загаданое число меньше')
    elif int(answer) < number:
        print('Загаданое число больше')
    else:
        print('Правильно! Ты угадал')
        break