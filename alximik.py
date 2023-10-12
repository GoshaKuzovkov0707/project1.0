from random import randint

class Zelie:
    def __init__(self, kach, name) -> None:
        self.kach = kach
        self.name = name

    def __str__(self) -> str:
        return f'Качество - {self.kach},имя - {self.name}'
    
    def __add__(self, other):
        result_name = self.name[0:len(self.name)//2] + other.name[len(other.name)//2:]
        resulf_kach = (self.kach + other.kach) // 2 
        self.cheak_kach(resulf_kach)
        return Zelie(resulf_kach, result_name) 
    
    def cheak_kach(self, resulf_kach):
        if resulf_kach <= 30:
            raise ValueError('Неправильное качество')

tot = Zelie(randint(0, 100), 'tot')

lol = Zelie(randint(0, 100), 'lol')

print(lol + tot)
print(type(Zelie))