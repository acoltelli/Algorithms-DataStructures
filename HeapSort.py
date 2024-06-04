import unittest


def heapify(arr, heapSize, rootIndex):
    largest = rootIndex
    leftChild = (2 * rootIndex) + 1
    rightChild = (2 * rootIndex) + 2

    # if the left child of the root is a valid index and is greater
    # than the current largest element, update the largest element
    if leftChild < heapSize and arr[leftChild] > arr[largest]:
        largest = leftChild

    # RHS
    if rightChild < heapSize and arr[rightChild] > arr[largest]:
        largest = rightChild

    # If the largest element is no longer the root element, swap them
    if largest != rootIndex:
        arr[rootIndex], arr[largest] = arr[largest], arr[rootIndex]
        # Heapify new root element to ensure it's the largest
        heapify(arr, heapSize, largest)


def heapSort(arr):
    # creates a max heap from the arr, and then removes the heaps root(largest) element
    for i in range(
        len(arr), -1, -1
    ):  # heapify runs backwards from the end of arr to its first element
        heapify(arr, len(arr), i)

    # Move the root of the max heap to the end of arr, thereby creating a sorted arr
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


class Test(unittest.TestCase):
    def testMergeSort(self):
        self.assertEqual(
            heapSort(
                [
                    3,
                    2,
                    1,
                    4,
                    6,
                    5,
                    7,
                    8,
                    9,
                    10,
                    11,
                    0,
                    200000000,
                    12,
                    13,
                    14,
                    15,
                    0,
                    16,
                    1,
                    1,
                    10,
                ]
            ),
            [
                0,
                0,
                1,
                1,
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                10,
                11,
                12,
                13,
                14,
                15,
                16,
                200000000,
            ],
        )
        self.assertEqual(heapSort([5, 0, 7, 2, 4, 8]), [0, 2, 4, 5, 7, 8])
        self.assertEqual(heapSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(heapSort([7]), [7])


if __name__ == "__main__":
    unittest.main()
