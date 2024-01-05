#Дана непустая строка S, длина которой N не превышает 10^6.
#Будем считать, что элементы строки нумеруются от 0 до N-1.
#Вычислите z-функцию z[i] для всех i от 0 до N-1.
#z[i] определяется как максимальная длина подстроки,
#начинающейся с позиции i и совпадающей с префиксом
#всей строки, z[0] = 0.
#Формат ввода
#Одна строка длины N, 0 < N <= 10^6, состоящая из
#прописных латинских букв.
#Формат вывода
#Выведите N чисел -- значения z-функции для каждой
#позиции, разделённые пробелом.

RawInput = open("input.txt","r")
Text = (RawInput.readline())[0:-1]
L = len(Text)
Z = [0] * L
Left = 0
Right = 0
print(Z[0], end=" ")
for T in range(1,L):
    Z[T] = max(0, min(Z[T - Left], Right - T))
    while (T+Z[T]<L and Text[Z[T]] == Text[T+Z[T]]):
        Z[T] += 1
    if T+Z[T]>Right:
        Left, Right = T, T+Z[T]
    print(Z[T], end=" ")
