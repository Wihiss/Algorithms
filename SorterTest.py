import SortingImpl

ar = [8,7,3,5,2,1,9,4,4]
# ar = [1,2,3]

sorter = SortingImpl.Sorter()

#sorter.doQuickSort(ar, 0, len(ar) - 1)
#sorter.doInsertionSort(ar)
sorter.doBubbleSort(ar)

print(ar)