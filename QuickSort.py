#Реализуйте быструю сортировку, используя
#алгоритм из предыдущей задачи.
#На каждом шаге выбирайте опорный элемент
#и выполняйте partition относительно него.
#Затем рекурсивно запуститесь от двух частей,
#на которые разбился исходный массив.
#Формат ввода
#В первой строке входного файла содержится
#число N -- количество элементов массива (0 ≤ N ≤ 10^6).
#Во второй строке содержатся N целых чисел a_i,
#разделенных пробелами (-10^9 <= a_i <= 10^9).
#Формат вывода
#Выведите результат сортировки, то есть N целых чисел,
#разделенных пробелами.

def Partition(DataArray, ClosedLeft, OpenRight, Pivot):
    PivotStart, GreaterStart, Current, Auxiliary = 0, 0, 0, 0
    for Current in range(ClosedLeft, OpenRight):    
        if DataArray[Current] < Pivot:
            if (PivotStart < GreaterStart and GreaterStart < Current):
                Auxiliary = DataArray[Current]
                DataArray[Current] = DataArray[GreaterStart]
                DataArray[GreaterStart] = DataArray[PivotStart]
                DataArray[PivotStart] = Auxiliary
            elif (PivotStart < Current and (GreaterStart == Current or GreaterStart == PivotStart)):
                DataArray[Current], DataArray[PivotStart] = DataArray[PivotStart], DataArray[Current]
            GreaterStart += 1
            PivotStart += 1
        elif DataArray[Current] == Pivot:
            Auxiliary = DataArray[GreaterStart]
            DataArray[GreaterStart] = DataArray[Current]
            DataArray[Current] = Auxiliary
            GreaterStart += 1
    return (DataArray, PivotStart, GreaterStart, Pivot)
 
def QuickSort(DataArray):
    if len(DataArray) < 2:
        return DataArray
    else:
        P = Partition(DataArray, 0, len(DataArray), (max(DataArray)+min(DataArray))//2)
        LeftArray = QuickSort(DataArray[:P[1]])
        RightArray = QuickSort(DataArray[P[2]:len(DataArray)])
        return LeftArray + [P[3] for j in range(P[1],P[2])] + RightArray
 
RawInput = open("input.txt","r")
N = int(RawInput.readline())
DataArray = (RawInput.readline()).split()
for Index in range(N):
    DataArray[Index] = int(DataArray[Index])
SortedArray = QuickSort(DataArray)
for j in range(N):
    print(SortedArray[j], end=" ")
