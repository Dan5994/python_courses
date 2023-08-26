# Задание 1
import random
import re

LIT = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']

class Iterra:
    def __init__(self, lit, num):
        self.num = num
        self.lit = lit
        self.count = 0
    
    def __iter__(self):
        return self 
    
    def __next__(self):
        if self.count > self.num:
            raise StopIteration
        name = ''.join([random.choice(LIT) for i in range(random.randint(1,10))])
        self.count += 1
        return name + str(self.count)
        
        
        
    def rand_letter(self):
        return random.choice(LIT)
    
# s = Iterra(LIT,3)
# print(next(s))


def gen_prog(i):
    while i < 100:
        i*=2
        yield i 

c=gen_prog(1)
print(next(c))
print(next(c))
print(next(c))




#Задание 2

# val_email = "(^[a-zA-Z0-9_.+-^*{|}_!~%]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
# c = input('введите email')
# res = re.match(val_email, c)
# print(res)
