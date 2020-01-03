# Class Sorter that provides implementation
# of several sorting algorithms.
class Sorter:

    def __init__(self):
        pass

    ########################################################################
    # QuickSort via Lomuto partition (pivot element - the last in the array)
    def doQuickSort(self, arr, startIndex, endIndex):
        if startIndex < endIndex:
            # Do partitioning, placing the pivot element in a correct index
            # (all elements of the left sub-array are less or equal to the pivot
            # and all elements of the right sub-array are greater than the pivot)
            pivotIndex = self.doQSPartition(arr, startIndex, endIndex)
            # Do sorting for the left sub-array
            self.doQuickSort(arr, startIndex, pivotIndex - 1)
            # Do sorting for the right sub-array
            self.doQuickSort(arr, pivotIndex + 1, endIndex)
        return arr
    
    def doQSPartition(self, arr, startIndex, endIndex):
        # Pivot is the last element
        pivot = arr[endIndex]
        # Index of the last element that less or equal the pivot element
        i = startIndex - 1
        # Loop variable
        j = startIndex
        # Iterate through the array
        while j <= endIndex - 1:
            # If element is less or equal the pivot,
            # swap it with an element that is greater the pivot
            if arr[j] <= pivot:
                i = i + 1
                self.swap(arr, i, j)
            j = j + 1
        # Place the pivot in a correct index (swap it with an element that
        # greater than the pivot)
        self.swap(arr, i + 1, endIndex)
        return i + 1
    ########################################################################

    ########################################################################
    # InsertionSort
    def doInsertionSort(self, arr):
        # Iterate through all array elements
        for i in range(1, len(arr)):
            j = i
            # Iterate back from element j to 0;
            # If j - 1 element greater than j, do swap
            while (j > 0 and (arr[j] < arr[j - 1])):
                self.swap(arr, j, j - 1)
                j = j - 1
    ########################################################################

    ########################################################################
    # BubbleSort
    def doBubbleSort(self, arr):
     if len(arr) == 1:
      return
     print("Source array: " + str(arr))
     moveOn = True
     endIndex = len(arr) - 1
     extIter = 0
     while moveOn:
      extIter += 1
      currIndex = 1
      swapped = False
      intIter = 0
      while currIndex <= endIndex:
       intIter += 1
       if arr[currIndex] < arr[currIndex - 1]:
        self.swap(arr, currIndex, currIndex - 1)
        swapped = True
       currIndex += 1
       print("Iteration " + str(extIter) + "," + str(intIter) + ": " + str(arr))
      endIndex -= 1
      moveOn = swapped
      print("---")
    ########################################################################

    def swap(self, arr, index1, index2):
        tmp = arr[index1]
        arr[index1] = arr[index2]
        arr[index2] = tmp
