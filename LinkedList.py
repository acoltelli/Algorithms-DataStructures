import unittest


class LinkedListNode:
    def __init__(self, data, nxt=None):
        self.data = data
        self.nxt = nxt

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current = self.head
        while current != None:
            yield current
            current = current.nxt

    def __getitem__(self, position):
        if position < len(self):
            index = 0
            current = self.head
            while index <= position:
                if index == position:
                    return current
                current = current.nxt
                index += 1

    def __str__(self):
        data = [str(x) for x in self]
        return " -> ".join(data)

    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.nxt
        return count

    def add(self, data):
        if self.head is None:
            self.tail = self.head = LinkedListNode(data)
        else:
            self.tail.nxt = LinkedListNode(data)
            self.tail = self.tail.nxt
        return self.tail

    def search(self, data):
        current = self.head
        while current != None:
            if current.data == data:
                return True
                break
            else:
                current = current.nxt
        if current is None:
            return False

    # CCI q 2.1
    def removeDuplicates(self):
        current = self.head
        seen = set([current.data])
        while current.nxt:
            if current.nxt.data in seen:
                current.nxt = current.nxt.nxt
            else:
                seen.add(current.nxt.data)
                current = current.nxt
        return self

    # CCI q 2.2
    def nthToLast(self, n):
        var = len(self) - n
        return self[var]

    # CCI q 2.3
    # object is deleted once there are no references to it
    def delete(self, data):
        current = self.head
        previous = None
        while current != None:
            if current.data == data:
                if previous != None:
                    previous.nxt = current.nxt
                else:
                    self.head = current.nxt
            previous = current
            current = current.nxt


# CCI q 2.4
def reverseAddition(list1, list2):
    var1 = [str(i) for i in list1]
    var1.reverse()
    var2 = [str(i) for i in list2]
    var2.reverse()
    solution = LinkedList()

    concat1 = int("".join(var1))
    concat2 = int("".join(var2))

    var = [i for i in str(concat1 + concat2)]
    for i in var:
        solution.add(i)
    return solution


####tests####

linkedListSample = LinkedList()
linkedListSample.add(1)
linkedListSample.add(2)
linkedListSample.add(0)
linkedListSample.add(1)
linkedListSample.add(0)
linkedListSample.add(1)
linkedListSample.add(8)

linkedListSample_ = LinkedList()
linkedListSample_.add(1)
linkedListSample_.add(2)
linkedListSample_.add(0)
linkedListSample_.add(1)
linkedListSample_.add(0)
linkedListSample_.add(1)
linkedListSample_.add(8)

lst1 = LinkedList()
lst1.add(3)
lst1.add(1)
lst1.add(5)
lst2 = LinkedList()
lst2.add(5)
lst2.add(9)
lst2.add(2)


class Test(unittest.TestCase):
    def testremoveDuplicates(self):
        self.assertEqual(
            str(LinkedList.removeDuplicates(linkedListSample)), "1 -> 2 -> 0 -> 8"
        )

    def testnthToLast(self):
        self.assertEqual(str(LinkedList.nthToLast(linkedListSample, 1)), "8")

    def testDelete(self):
        LinkedList.delete(linkedListSample_, 8)
        self.assertEqual(str(linkedListSample_), "1 -> 2 -> 0 -> 1 -> 0 -> 1")
        LinkedList.delete(linkedListSample_, 0)
        self.assertEqual(str(linkedListSample_), "1 -> 2 -> 1 -> 1")

    def testassertEqual(self):
        self.assertEqual(str(reverseAddition(lst1, lst2)), "8 -> 0 -> 8")


if __name__ == "__main__":
    unittest.main()
