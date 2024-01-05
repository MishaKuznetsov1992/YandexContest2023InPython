#Реализуйте сортировку слиянием, используя
#алгоритм из предыдущей задачи.
#На каждом шаге делите массив на две части,
#сортируйте их независимо и сливайте
#с помощью уже реализованной функции.
#Формат ввода
#В первой строке входного файла содержится,
#число N -- количество элементов массива (0 <= N <= 10^6).
#Во второй строке содержатся N целых чисел a_i,
#разделенных пробелами (-10^9 <= ai <= 10^9).
#Формат вывода
#Выведите результат сортировки, то есть N целых чисел,
#разделенных пробелами, в порядке неубывания.

def Merge(ListA, ListB):
    ListC = []
    IndexA, IndexB = 0, 0
    while not(IndexA == len(ListA) and IndexB == len(ListB)):
        if (IndexA < len(ListA) and IndexB < len(ListB)):
            if ListA[IndexA] > ListB[IndexB]:
                ListC.append(ListB[IndexB])
                IndexB += 1
            else:
                ListC.append(ListA[IndexA])
                IndexA += 1
        elif (IndexA < len(ListA)):
            ListC.append(ListA[IndexA])
            IndexA += 1
        else:
            ListC.append(ListB[IndexB])
            IndexB += 1
    return ListC

def MergeSort(DataArray):
    if len(DataArray) < 2:
        return DataArray
    else:
        ListA = MergeSort(DataArray[:len(DataArray)//2])
        ListB = MergeSort(DataArray[len(DataArray)//2:len(DataArray)])
        return Merge(ListA, ListB)

RawInput = open("input.txt","r")
N = int(RawInput.readline())
DataArray = (RawInput.readline()).split()
for Index in range(N):
    DataArray[Index] = int(DataArray[Index])
SortedArray = MergeSort(DataArray)
for Index in range(N):
    print(SortedArray[Index], end=" ")
