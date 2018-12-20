import unittest

def bubbleSort(arr):
  for i in range(0, len(arr)):
    for j in range(0,len(arr)-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
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



###tests###

class Test(unittest.TestCase):   
    def testBubbleSort(self):
      self.assertEqual(bubbleSort([3, 1, 2, 4, 6, 5, 3, 1]), [1, 1, 2, 3, 3, 4, 5, 6])
      self.assertEqual(bubbleSort([3, 1, 0]), [0, 1, 3])

    def testInsertionSort(self):
      self.assertEqual(insertionSort([3, 1, 2, 4, 6, 5, 3, 1]), [1, 1, 2, 3, 3, 4, 5, 6])
      self.assertEqual(insertionSort([0, 1, 2, 4, 6, 5, 3]),[0, 1, 2, 3, 4, 5, 6])

    def testQuickSort(self):
      self.assertEqual(quickSort([10,9,8,7,6,5,4,3,2,1]), [1,2,3,4,5,6,7,8,9,10])
      self.assertEqual(quickSort([7,7,7,7,7,7,7]), [7,7,7,7,7,7,7])
      self.assertEqual(quickSort([5,4,3,2,1, 10, 0, 5,5, 0]), [0, 0, 1, 2, 3, 4, 5, 5, 5, 10])
      self.assertEqual(quickSort([5,5,1,4,3,2,5,1, 10,0,0]), [0, 0, 1, 1, 2, 3, 4, 5, 5, 5, 10])

    def testQuickSortMid(self):
      self.assertEqual(quickSortMid([10,9,8,7,6,5,4,3,2,1]), [1,2,3,4,5,6,7,8,9,10])
      self.assertEqual(quickSort([7,7,7,7,7,7,7]), [7,7,7,7,7,7,7])
      self.assertEqual(quickSortMid([5,4,3,2,1, 10, 0, 5,5, 0]), [0, 0, 1, 2, 3, 4, 5, 5, 5, 10])
      self.assertEqual(quickSortMid([5,5,1,4,3,2,5,1, 10,0,0]), [0, 0, 1, 1, 2, 3, 4, 5, 5, 5, 10])


if __name__ == "__main__":
    unittest.main()




