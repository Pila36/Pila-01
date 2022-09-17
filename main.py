a = int(input("Введите А:"))
b = int(input("Введите В:"))
c = int(input("Введите С:"))

if (a>b and a>c):
    print("А больше всех. А = ", a)
elif (b>a and b>c):
    print("B больше всех. B = ", b)
elif (c>a and c>b ):
    print("C больше всех. C = ", c)
else:
    print("Они равны")