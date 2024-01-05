#Поразрядная сортировка является одним из видов
#сортировки, которые работают практически за
#линейное от размера сортируемого массива время.
#Такая скорость достигается за счет того, что эта
#сортировка использует внутреннюю структуру
#сортируемых объектов. Изначально этот алгоритм
#использовался для сортировки перфокарт.
#Первая его компьютерная реализация была создана
#в университете MIT Гарольдом Сьюардом (Harold Н. Seward).
#Опишем алгоритм подробнее. Пусть задан массив
#строк s1 , ..., si причём все строки имеют одинаковую
#длину m. Работа алгоритма состоит из m фаз. На i-ой фазе
#строки сортируются по i-ой с конца букве. Происходит
#это следующим образом. Будем, для простоты, в этой задаче
#рассматривать строки из цифр от 0 до 9. Для каждой цифры
#создается "корзина" ("bucket"), после чего строки si
#распределяются по "корзинам" в соответствии с i-ой
#цифрой с конца. Строки, у которых i-ая с конца цифра
#равна j, попадают в j-ую корзину (например, строка 123
#на первой фазе попадет в третью корзину,
#на второй -- во вторую, на третьей — в первую).
#После этого элементы извлекаются из корзин в порядке
#увеличения номера корзины. Таким образом, после первой
#фазы строки отсортированы по последней цифре, после
#двух фаз -- по двум последним, ..., после m фаз -- по всем.
#При этом важно, чтобы элементы в корзинах сохраняли тот же
#порядок, что и в исходном массиве (до начала этой фазы).
#Например, если массив до первой фазы имеет вид:
#111, 112, 211, 311, то элементы по корзинам распределятся
#следующим образом: в первой корзине будет. 111, 211, 311,
#а во второй: 112. Напишите программу, детально показывающую
#работу этого алгоритма на заданном массиве.
#Формат ввода
#Первая строка входного файла содержит целое число n (1 <= n <= 1000).
#Последующие n строк содержат каждая по одной строке si.
#Длины всех si одинаковы и не превосходят 20. Все si состоят
#только из цифр от 0 до 9.
#Формат вывода
#В выходной файл выведите исходный массив строк в,
#состояние «корзин» после распределения элементов по ним
#для каждой фазы и отсортированный массив. Следуйте формату,
#приведенному в примере.
#Пример
#Ввод
#9
#12
#32
#45
#67
#98
#29
#61
#35
#09
#Вывод
#Initial array:
#12, 32, 45, 67, 98, 29, 61, 35, 09
#**********
#Phase 1
#Bucket 0: empty
#Bucket 1: 61
#Bucket 2: 12, 32
#Bucket 3: empty
#Bucket 4: empty
#Bucket 5: 45, 35
#Bucket 6: empty
#Bucket 7: 67
#Bucket 8: 98
#Bucket 9: 29, 09
#**********
#Phase 2
#Bucket 0: 09
#Bucket 1: 12
#Bucket 2: 29
#Bucket 3: 32, 35
#Bucket 4: 45
#Bucket 5: empty
#Bucket 6: 61, 67
#Bucket 7: empty
#Bucket 8: empty
#Bucket 9: 98
#**********
#Sorted array:
#09, 12, 29, 32, 35, 45, 61, 67, 98

RawInput = open("input.txt","r")
N = int(RawInput.readline())
DataArray = []
Buckets = [[] for j in range(10)]
print("Initial array:")
for Index in range(N):
    DataArray.append((RawInput.readline()).split()[0])
    if Index < N-1:
        print(DataArray[-1], end=", ")
    else:
        print(DataArray[-1])
Phases = len(DataArray[0])
for Phase in range(Phases):
    print("**********")
    print("Phase "+str(Phase+1))
    for Index in range(N):
        Buckets[int(DataArray[Index][Phases-1-Phase])].append(DataArray[Index])
    for j in range(10):
        if Buckets[j] == []:
            print("Bucket "+str(j)+": empty")
        else:
            print("Bucket "+str(j)+":", end=" ")
            for Item in range(len(Buckets[j])):
                if Item < len(Buckets[j])-1:
                    print(Buckets[j][Item], end=", ")
                else:
                    print(Buckets[j][Item])
    DataArray = []
    for j in range(10):
        DataArray.extend(Buckets[j])
        Buckets[j] = []
print("**********")
print("Sorted array:")
for Index in range(N):
    if Index < N-1:
        print(DataArray[Index], end=", ")
    else:
        print(DataArray[Index])
