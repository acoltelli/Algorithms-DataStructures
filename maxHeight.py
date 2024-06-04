import unittest


# A binary tree node
class Node:
    # node constructor
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# compute number of nodes along the longest path from the root node down to the farthest leaf node
def maxDepth(node):
    if node is None:
        return 0
    else:
        # depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
        # return the larger one
        if lDepth > rDepth:
            return lDepth + 1
        else:
            return rDepth + 1


class Test(unittest.TestCase):
    def testMaxDepth(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)

        self.assertEqual(maxDepth(root), 3)


if __name__ == "__main__":
    unittest.main()
