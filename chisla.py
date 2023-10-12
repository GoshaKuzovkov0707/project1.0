# money = 1234567890

def ca_ba(money):
    fed = {}
    if money // 1000 > 0:
        fed['Тысяча'] = money // 1000
        money = money % 1000
    if money // 500 > 0:
        fed['Пятьсот'] = money // 500
        money = money % 500
    if money // 100 > 0:
        fed['Сто'] = money // 100
        money = money % 100
    if money // 50 > 0:
        fed['Пятьдесят'] = money // 50
        money = money % 50
    if money // 10 > 0:
        fed['Десять'] = money // 10
        money = money % 10
    if money // 5 > 0:
        fed['Пять'] = money // 5
        money = money % 5
    if money // 1 > 0:
        fed['Рублей'] = money // 1
        money = money % 1
    print('f ', money)
    return fed

# print(ca_ba(money))
# print('gl ', money)


def f_u(lisd):
    def a():
        ...
    chet = []
    nechet = []
    for i in lisd:
        if i % 2 == 0:
            chet.append(i)
        else:
            nechet.append(i)
    # print(chet, nechet)
    if len(chet) > len(nechet):
        return nechet
    elif len(chet) < len(nechet):
        return chet
    else:
        return f_u([1, 3, 5, 8, 10, 4])


print(f_u([6, 2, 8, 5, 4]))
print(f_u([1, 3, 5, 7, 9, 4]))
print(f_u([1, 3, 5, 8, 10, 4]))

