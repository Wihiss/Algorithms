# Class Search provides implementation
# of several search algorithms.
class Search:

    def __init__(self):
     pass

    def doBinarySearch(self, arr, target):
     # If there is the only element, return 0th index
     if len(arr) == 1:
      self.bsCheckSingleElement(arr, target, 0)
      return 0
     #

     # Launch loop recursively
     return self.bsIntLoop(arr, target, 0, len(arr) - 1)

    # Internal loop
    def bsIntLoop(self, arr, target, start, end):
     # Check if the only element left
     if end == start:
      self.bsCheckSingleElement(arr, target, start)
      return start
     #

     # Get mid element index
     currArrLenth = end - start + 1
     mid = start + int(currArrLenth / 2) - 1
     #

     # Do recursive search through 'left' or 'right' half
     if arr[mid] >= target:
      return self.bsIntLoop(arr, target, start, mid)

     return self.bsIntLoop(arr, target, mid + 1, end)
     #
    
    # Check if particular element is equal to target
    def bsCheckSingleElement(self, arr, target, index):
     if arr[index] != target:
      raise RuntimeError(str(target) + " not found")