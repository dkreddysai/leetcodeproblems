class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None
def minDepth(root):
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return 1
     
    if root.left is None:
        return minDepth(root.right)+1
    if root.right is None:
        return minDepth(root.left) +1
     
    return min(minDepth(root.left), minDepth(root.right))+1
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(minDepth(root))
