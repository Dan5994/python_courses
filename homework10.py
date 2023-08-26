class InvalidError(Exception):
    pass



class Calculator:
    @classmethod
    def sum(cls, a, b):
        return a + b
    @classmethod
    def subtrack(cls, a, b):
        return a - b
    @classmethod
    def multiply(cls, a, b):
        return a * b
    @classmethod
    def divide(cls, a, b):
        return a / b


OPERATOR_ZNAKA = {
    '+': Calculator.sum,
    '-': Calculator.subtrack,
    '*': Calculator.multiply,
    '/': Calculator.divide
}
try:
    x = int(input('Введите первое число: '))
    y = int(input('Введите второе число: '))
    shag = input('Введите действие (+, -, *, /): ')   
    result = OPERATOR_ZNAKA[shag](x, y)
    if x == 1:
        raise InvalidError(f'Аргумент равен {x}')
    print(result)
except ValueError as etc:
    print(f'Введена строка: {etc}')
except ZeroDivisionError as etc:
    print(f'Ошибка {etc}')
except KeyError as etc:
    print(f'Неверный ключ {etc}')

# import pdb; pdb.set_trace()