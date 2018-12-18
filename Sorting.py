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

 


###tests###

class Test(unittest.TestCase):   
    def testBubbleSort(self):
      self.assertEqual(bubbleSort([3, 1, 2, 4, 6, 5, 3, 1]), [1, 1, 2, 3, 3, 4, 5, 6])
      self.assertEqual(bubbleSort([3, 1, 0]), [0, 1, 3])

    def testInsertionSort(self):
      self.assertEqual(insertionSort([3, 1, 2, 4, 6, 5, 3, 1]), [1, 1, 2, 3, 3, 4, 5, 6])
      self.assertEqual(insertionSort([0, 1, 2, 4, 6, 5, 3]),[0, 1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()




