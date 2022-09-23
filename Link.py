print('Количество этажей')
N = int(input())
print('Вы ввели ', N)

print('Стоимость одной квартиры')
X = int(input())
print('Вы ввели ', X)

print('Коэффициент')
M = int(input())
print('Вы ввели ', M)

P = N // M
print ('Повышение цен будет', P)

S = 0
Sum = 0

for i in range(P):
    S = (X + 1000 * i) * M
    Sum = Sum + S
    print(i, S)
Sum = Sum + N % M * (X + 1000 * M)

print(Sum)





