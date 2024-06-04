import unittest


# CCI q 3.4
def towersOfHanoi(n, first, last, middle):
    if n > 0:
        towersOfHanoi(n - 1, first, middle, last)
        last.append(first.pop())
        towersOfHanoi(
            n - 1, middle, last, first
        )  # move n - 1 disks that are left on middle to last
    return (first, middle, last)


class Test(unittest.TestCase):
    def testTowersofHanoi(self):
        n = 3
        A = [i for i in range(n, 0, -1)]
        B = []
        C = []
        self.assertEqual(towersOfHanoi(n, A, B, C), ([], [], [3, 2, 1]))
        n = 20
        A = [i for i in range(n, 0, -1)]
        B = []
        C = []
        self.assertEqual(
            towersOfHanoi(n, A, B, C),
            (
                [],
                [],
                [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
            ),
        )
        n = 0
        A = [i for i in range(n, 0, -1)]
        B = []
        C = []
        self.assertEqual(towersOfHanoi(n, A, B, C), ([], [], []))
        n = 1
        A = [i for i in range(n, 0, -1)]
        B = []
        C = []
        self.assertEqual(towersOfHanoi(n, A, B, C), ([], [], [1]))


if __name__ == "__main__":
    unittest.main()
