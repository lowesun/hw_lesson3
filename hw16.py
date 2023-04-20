# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
N = abs(int(input('Введите количество элементов списка N: ')))
A_entered = input("Введите через пробел элементы списка: ").split()
A_num = list(map(int, A_entered))
if len(A_num) != N:
    print('Введенные элементы не соответствуют заявленному количеству!')
else:
    X = int(input('Введите число X, которое необходимо найти в списке: '))
    count = 0
    for i in range(N):
        if A_num[i] == X:
            count += 1
    print(f'Число {X} встречается в списке N {count} раз') 