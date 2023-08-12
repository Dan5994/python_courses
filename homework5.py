# Задание 1
note = lambda num=int(input('Введите число: ')): print('Чётное') if num % 2 == 0 else print('Нечётное')
note()

# Задание 2
list_1 = [2, 3, 7, 133, 5345, 52512, 453345]
print(list(map(lambda a: str(a), list_1)))

# # Задание 3
kort = ('55', 'собака', '545', 'бабка', 'казак')
res = tuple(filter(lambda pol: str(pol) == str(pol)[::-1], kort))
print(res)

# Задание 4
from datetime import datetime

res = [-1, -5, -11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def time_performance(func):
    def wrapper(golf):
        startfunk = datetime.now()
        bid = func(golf)
        finishfunc = datetime.now()
        time = finishfunc - startfunk
        print(f'Время выполнения: {time}')
        return bid

    return wrapper


@time_performance
def some_function(text):
    print(text)


some_function('Функция')


@time_performance
def func_filt(gem):
    print(list(filter(lambda x: x < 0, res)))


func_filt(res)


# Задание 5
def examination_str(number: str):
    search = number.find(".")
    if search > 0:
        sumbl = number[:search]
        sumblr = number[search + 1:]
        if sumbl.isdigit() and sumblr.isdigit():
            print("Вы ввели положительное дробное число :", float(number))
        elif sumbl[1:].isdigit() and sumbl[0] == "-" and sumblr.isdigit():
            print("Вы ввели отрицательное дробное число :", float(number))
        else:
            print("Вы ввели некоректное число!")
    elif number.isdigit():
        print("Вы ввели положительное целое число :", int(number))
    elif number[0] == "-" and number[1:].isdigit():
        print("Вы ввели отрицательное целое число :", int(number))
    else:
        print("Вы ввели некоректное число!")


examination_str('-5.4')
