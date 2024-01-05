#Строка S была записана много раз подряд,
#после чего от получившейся строки взяли префикс
#и дали вам. Ваша задача определить минимально
#возможную длину исходной строки S.
#Формат ввода
#В первой и единственной строке входного файла
#записана строка, которая содержит только латинские
#буквы, длина строки не превышает 50000 символов.
#Формат вывода
#Выведите ответ на задачу.

Modulus = 10 ** 9 + 7
Radix = 257
Beginning = ord("A") - 1
RawInput = open("input.txt","r")
Text = (RawInput.readline())[0:-1]
Hashes = [0]
Powers = [1]
L = len(Text)
for Index in range(L):
    Hashes.append((Hashes[-1] * Radix + ord(Text[Index]) - Beginning) % Modulus)
    Powers.append((Powers[-1] * Radix) % Modulus)
for T in range(1, L+1):
    if ((Hashes[L-T] + Hashes[T] * Powers[L-T] - Hashes[L]) % Modulus == 0):
        break
print(T)
