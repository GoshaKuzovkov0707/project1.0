asd1 = [1, 2, 3, 4, 58, 77, 109, 532873, 8]

def poisck(asd2, num):
    asd3 = [i for i in asd2 if not (i % 1)]
    print(asd3)
    for i in asd2:
        if i == num:
            return True
    return False

print(poisck(asd1, 1))