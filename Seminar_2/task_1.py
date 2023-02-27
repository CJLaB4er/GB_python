n = int(input())
factorial = 1
while n > 0:
    factorial *= n
    n-=1

print(f"Факториал числа {n} равен {factorial}")