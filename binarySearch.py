import unittest


# recursive
def binarySearch(arr, n):
    if len(arr) == 0:
        return False

    mid = len(arr) / 2
    if arr[mid] == n:
        return True
    else:
        if n > arr[mid]:
            return binarySearch(arr[mid + 1 :], n)
        else:
            return binarySearch(arr[:mid], n)


# iterative
def bS(arr, n):
    first = 0
    last = len(arr) - 1
    seen = False

    while first <= last and seen == False:
        mid = (first + last) / 2
        if arr[mid] == n:
            seen = True
        else:
            if n < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return seen


class Test(unittest.TestCase):
    def testBSRecursive(self):
        arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        arr = sorted(arr)
        self.assertEqual(binarySearch(arr, 3), True)
        self.assertEqual(binarySearch(arr, -1), False)
        self.assertEqual(binarySearch(arr, 0), True)
        arr1 = [-13, 0, 15, 1009, -7]
        arr1 = sorted(arr1)
        self.assertEqual(binarySearch(arr1, -13), True)
        self.assertEqual(binarySearch(arr1, 0), True)
        self.assertEqual(binarySearch(arr1, 27), False)
        self.assertEqual(binarySearch(arr1, -27), False)
        arr2 = []
        self.assertEqual(binarySearch(arr2, 7), False)

    def testBSIterative(self):
        arr = [-13, 0, -2, 15, 1009, -7]
        arr = sorted(arr)
        self.assertEqual(bS(arr, -2), True)
        self.assertEqual(bS(arr, -13), True)
        arr1 = []
        self.assertEqual(bS(arr1, -2), False)


if __name__ == "__main__":
    unittest.main()
