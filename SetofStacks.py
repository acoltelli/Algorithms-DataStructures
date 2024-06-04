import unittest


# CCI q 3.3
class SetOfStacks:
    def __init__(self, n):
        self.size = n  # size which once exceeded a new stack begins
        self.stacks = [[]]

    def __str__(self):
        return str(self.stacks)

    def push(self, data):
        if len(self.stacks[-1]) == self.size:
            self.stacks.append([])
        self.stacks[-1].append(data)

    def pop(self):
        if self.stacks == [[]]:
            exit("Stack Underflow")
        var = self.stacks[-1].pop()
        return var

    def popAt(self, index):  # index indicates which number sub-stack should be .pop()
        var = self.stacks[index].pop()
        return var


###tests###


class Test(unittest.TestCase):
    def testSetOfStacks(self):
        var = SetOfStacks(2)
        for i in xrange(1, 8):
            var.push(i)
        bar = SetOfStacks(3)
        for i in xrange(1, 8):
            bar.push(i)

        self.assertEqual(var.stacks, [[1, 2], [3, 4], [5, 6], [7]])
        self.assertEqual(bar.stacks, [[1, 2, 3], [4, 5, 6], [7]])

    def testPush(self):
        var = SetOfStacks(2)
        for i in xrange(1, 9):
            var.push(i)
        self.assertEqual(var.stacks, [[1, 2], [3, 4], [5, 6], [7, 8]])
        var.push(9)
        self.assertEqual(var.stacks, [[1, 2], [3, 4], [5, 6], [7, 8], [9]])

    def testPop(self):
        var = SetOfStacks(2)
        for i in xrange(1, 8):
            var.push(i)
        bar = SetOfStacks(0)

        self.assertEqual(var.pop(), 7)
        with self.assertRaises(SystemExit):
            bar.pop()

    def testPopAt(self):
        var = SetOfStacks(2)
        for i in xrange(1, 8):
            var.push(i)
        bar = SetOfStacks(0)

        self.assertEqual(var.popAt(2), 6)
        self.assertEqual(var.popAt(0), 2)
        with self.assertRaises(SystemExit):
            bar.pop()


if __name__ == "__main__":
    unittest.main()
