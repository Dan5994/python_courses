class Date:
    @classmethod
    def calculate(cls, *args):
        if len(args) < 2:
            return None
        return cls.func(cls.func_2(*args[1::2]), cls.func_1(*args[::2]))

    @staticmethod
    def func(a,b):
        return a - b
        
    @staticmethod
    def func_1(*args):
        res=1
        for numbers in args:
            res *= numbers
        return res
    
    @staticmethod
    def func_2(*args):
        fj=1
        for numbers in args:
            fj *= numbers
        return fj
        

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(Date.calculate(*list))