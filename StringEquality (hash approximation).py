#Дана строка S, состоящая из строчных латинских букв.
#Определите, совпадают ли строки одинаковой длины L,
#начинающиеся с позиций A и B.
#Формат ввода
#В первой строке записана S (1 <= |S| <= 2*10^5),
#состоящая из строчных латинских букв.
#Во второй строке записано число Q
#(1 <= Q <= 2*10^5) -- количество запросов.
#В следющих Q строках записаны запросы: целые числа
#L, A и B (1 <= L <= |S|, 0 <= (A, B) <= (|S| - L)) -- длина подстрок
#и позиции, с которых они начинаются.
#Формат вывода
#Если строки совпадают -- выведите "yes", иначе -- "no".

Modulus = 1000000007
Radix = 257
Beginning = ord("a") - 1
RawInput = open("input.txt","r")
Text = (RawInput.readline())
Q = int(RawInput.readline())
Hashes = [0]
Powers = [1]
for Index in range(len(Text)-1):
    Hashes.append((Hashes[-1] * Radix + ord(Text[Index]) - Beginning) % Modulus)
    Powers.append((Powers[-1] * Radix) % Modulus)
for Query in range(Q):
    LAB = (RawInput.readline()).split()
    L = int(LAB[0])
    A = int(LAB[1])
    B = int(LAB[2])
    if ((Hashes[A+L] - Hashes[B+L] - (Hashes[A] - Hashes[B]) * Powers[L]) % Modulus == 0):
        print("yes")
    else:
        print("no")
