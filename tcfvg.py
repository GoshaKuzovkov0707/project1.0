# def a(x):
#     print(x)
#     if x == 0.0:
#         return x
#     return a(x-0.2)

# a(5)

class Cat():
    a = 5

    def __init__(self, name, color):
        self.name = name
        self.color = color

    # def getter_name(self):
    #     if role == 'administrator':
            # return self.__name
    #     else:
    #         raise ValueError
    # one = 100
    # two = 200

    # def __add__ (one, two):
    #     result_name = one.name[0:len(one.name)//2] + two.name[len(two.name)//2:]
    #     result_color = one.color[0:len(one.color)//2] + two.color[len(two.color)//2:]
    #     return Cat(result_name, result_color)

    # def __str__(self) -> str:
    #     return f'Name: {self.name}, color: {self.color}'
    
    def sleep(self):
        print(f'Z z z _кот по имени {self.name} спит_')

# print(type(None))

fluffy = Cat('Snowbal', 'white')


utf8 = Cat('Bananaq', 'yellow')

# print(fluffy.getter_name())
print(fluffy.__dict__, fluffy.a, utf8.a)
# print(utf8)
# print(fluffy)

# print(fluffy)
# fluffy.name = 'evede'
# fluffy.color = 'green'
# print(fluffy.name)
# print(fluffy.color)
print(utf8.name)
# print(utf8.color)
# print(utf8.two)
# utf8.sleep()
# Cat.sleep(fluffy)

print(utf8 + fluffy)     