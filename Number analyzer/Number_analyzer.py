number = int(input("Введите пятизначное целое число "))
n1 = number // 10000
n2 = number // 1000 % 10
n3 = number // 100 % 10
n4 = number // 10 % 10
n5 = number % 10
print((n4 ** n5) * n3 / (n1 - n2))