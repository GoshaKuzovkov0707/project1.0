kot=[]
while True:
    a=input('Что вы хотите добавить в список? \n Если закончили напишите - выход ')
    if a.lower() =='выход':
       break 
    kot.append(a)
    print(f'Текущий список покупок содержит {kot}')


