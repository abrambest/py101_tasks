"""
Программа выводит на экран числа от 1 до 100 включительно, с новой строки.

Если число кратно трём, то вместо этого числа программа выводит слово "zip"
Если чисто кратно пяти, то вместо этого числа выводится слово "zap"
Если число кратно пятнадцати, то вместо этого числа выводится слово "zip-zap"

Тебе может понадобиться цикл for и ветвления
"""

if __name__ == '__main__':
    pass
for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print("zip-zap", end=' ')
    elif x % 3 == 0:
        print("zip", end=' ')
    elif x % 5 == 0:
        print("zap", end=' ')
    else:
        print(x, end=' ')