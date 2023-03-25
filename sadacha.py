def cals_savings(s, t=1, i=0.02):
    for a in range(t):
        pros = s * i
        s += pros
        print(f'На вашем счету {s}')
    print(f'Ваш итоговый счет в банке {s}')

def iop():
    i = int(input('Под какой процент вы кладёте деньги: ')) / 100
    s = int(input('Сколько вы хотите положить денег в банк: '))
    t = int(input('На сколько лет : '))
    cals_savings(s, t, i)

iop()

    
