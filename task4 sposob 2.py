a = int(input("Введите год: "))
if a % 400 == 0:
    print('Високосный')
elif a % 100 == 0:
    print('Не високосный')
elif a % 4 == 0:
    print('Високосный')
else:
    print('Не високосный')