import SearchImpl
import SortingImpl

ar = [8,7,3,5,2,1,9,4,4]
# ar = [3,1,2]

sorter = SortingImpl.Sorter()
sorter.doBubbleSort(ar)

search = SearchImpl.Search()

target = 2
index = search.doBinarySearch(ar, target)

print(str(target) + " found at index " + str(index))