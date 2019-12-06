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
        return 0 ;
    else :
        # depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
        # return the larger one
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1
