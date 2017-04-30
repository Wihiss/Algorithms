import SortingImpl

ar = [3,7,8,5,2,1,9,4,4]

sorter = SortingImpl.Sorter()

#sorter.doQuickSort(ar, 0, len(ar) - 1)
sorter.doInsertionSort(ar)

print(ar)