import unittest

def bubbleSort(arr):
    swap = True
    while swap:
        swap = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap = True
    return arr

def insertionSort(arr):
    for i in range(1,len(arr)):
        current = arr[i]
        while i > 0 and arr[i-1] > current:
            arr[i] = arr[i-1]
            i -= 1
        arr[i] = current
    return arr

def quickSort(arr):   #pivot point is first element of array
    if len(arr) == 0:
      return arr
    else:
      return quickSort([i for i in arr[1:] if i < arr[0]]) + [i for i in arr if i == arr[0]] + quickSort([i for i in arr[1:] if i > arr[0]])

def quickSortMid(arr):   #pivot point is midpoint of array
    if len(arr) == 0:
      return arr
    else:
      return quickSortMid([i for i in arr if i < arr[len(arr)/2]]) + [i for i in arr if i == arr[len(arr)/2]] + quickSortMid([i for i in arr if i > arr[len(arr)/2]])

def mergeSort(arr):
    if len(arr) == 1 :   #end recursions once len partitions is decreased to one
      return arr
    else:
      merged = []
      left = mergeSort(arr[:len(arr)/2])   #divide into two partitions and recursively sort
      right = mergeSort(arr[len(arr)/2:])

      while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
          merged.append(right.pop(0))   #sort elements in partitions
        else:
          merged.append(left.pop(0))

      merged.extend(left + right)   #merge the sorted partitions(partially sorted if len>1)
      return merged



###tests###

class Test(unittest.TestCase):
    def testBubbleSort(self):
      self.assertEqual(bubbleSort([3, 1, 2, 4, 6, 5, 3, 1]), [1, 1, 2, 3, 3, 4, 5, 6])
      self.assertEqual(bubbleSort([3, 1, 0]), [0, 1, 3])
      self.assertEqual(bubbleSort([1,2,3]),[1,2,3])
      self.assertEqual(bubbleSort([0]),[0])

    def testInsertionSort(self):
      self.assertEqual(insertionSort([3, 1, 2, 4, 6, 5, 3, 1]), [1, 1, 2, 3, 3, 4, 5, 6])
      self.assertEqual(insertionSort([0, 1, 2, 4, 6, 5, 3]),[0, 1, 2, 3, 4, 5, 6])
      self.assertEqual(insertionSort([1,2,3]),[1,2,3])
      self.assertEqual(insertionSort([7]),[7])

    def testQuickSort(self):
      self.assertEqual(quickSort([10,9,8,7,6,5,4,3,2,1]), [1,2,3,4,5,6,7,8,9,10])
      self.assertEqual(quickSort([7,7,7,7,7,7,7]), [7,7,7,7,7,7,7])
      self.assertEqual(quickSort([5,4,3,2,1, 10, 0, 5,5, 0]), [0, 0, 1, 2, 3, 4, 5, 5, 5, 10])
      self.assertEqual(quickSort([5,5,1,4,3,2,5,1, 10,0,0]), [0, 0, 1, 1, 2, 3, 4, 5, 5, 5, 10])
      self.assertEqual(quickSort([1,2,3,4,5]), [1,2,3,4,5])
      self.assertEqual(quickSort([7]), [7])

    def testQuickSortMid(self):
      self.assertEqual(quickSortMid([10,9,8,7,6,5,4,3,2,1]), [1,2,3,4,5,6,7,8,9,10])
      self.assertEqual(quickSort([7,7,7,7,7,7,7]), [7,7,7,7,7,7,7])
      self.assertEqual(quickSortMid([5,4,3,2,1, 10, 0, 5,5, 0]), [0, 0, 1, 2, 3, 4, 5, 5, 5, 10])
      self.assertEqual(quickSortMid([5,5,1,4,3,2,5,1, 10,0,0]), [0, 0, 1, 1, 2, 3, 4, 5, 5, 5, 10])
      self.assertEqual(quickSortMid([1,2,3,4,5]), [1,2,3,4,5])
      self.assertEqual(quickSortMid([7]), [7])

    def testMergeSort(self):
      self.assertEqual(mergeSort([3,2,1, 4,6,5,7,8,9,10,11,0,200000000,12,13,14,15,0,16,1,1,10]),[0,0,1,1,1,2,3,4,5,6,7,8,9,10,10,11,12,13,14,15,16,200000000])
      self.assertEqual(mergeSort([5,0,7,2,4,8]), [0,2,4,5,7,8])
      self.assertEqual(mergeSort([1,2,3,4,5]), [1,2,3,4,5])
      self.assertEqual(mergeSort([7]),[7])


if __name__ == "__main__":
    unittest.main()
