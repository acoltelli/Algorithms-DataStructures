import unittest

#resursive 
def binarySearch(arr, n):
    if len(arr) == 0:
        return False

    arr = sorted(arr)
    mid = len(arr) / 2
    if arr[mid] == n:
      return True
    else:
      if n > arr[mid]:
      	return binarySearch(arr[mid + 1:], n)
      else:
      	return binarySearch(arr[:mid], n)

        
class Test(unittest.TestCase): 
	def testBSRecursive(self):
		arr = [0, 1, 2 ,3 , 4, 5, 6,7, 8, 9]
		self.assertEqual(binarySearch(arr, 3), True)
		self.assertEqual(binarySearch(arr, -1), False)
		self.assertEqual(binarySearch(arr, 0), True)
		arr1 = [-13, 0 , 15, 1009, -7]
		self.assertEqual(binarySearch(arr1, -13), True)
		self.assertEqual(binarySearch(arr1, 0), True)
		self.assertEqual(binarySearch(arr1, 27), False)
		self.assertEqual(binarySearch(arr1, -27), False)




if __name__ == "__main__":
    unittest.main()

