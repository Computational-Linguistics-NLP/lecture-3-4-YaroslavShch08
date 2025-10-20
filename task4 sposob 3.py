a = int(input("Введите год: "))
if a % 400 == 0:
    print("Високосный")
else:
    if a % 100 == 0:
        print("Не високосный")
    else:
        if a % 4 == 0:
            print("Високосный")
        else:
            print("Не високосный")