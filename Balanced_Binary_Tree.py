#https://leetcode.com/problems/balanced-binary-tree/submissions/
#Balanced Binary Tree
# Definition for a binary tree node
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BalancedBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value <= node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def is_balanced(self):
        return self._is_balanced_recursive(self.root)

    def _is_balanced_recursive(self, node):
        if node is None:
            return True
        
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        
        if abs(left_height - right_height) <= 1 and self._is_balanced_recursive(node.left) and self._is_balanced_recursive(node.right):
            return True
        
        return False

    def _height(self, node):
        if node is None:
            return 0
        
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        
        return 1 + max(left_height, right_height)

tree = BalancedBinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.insert(12)
tree.insert(18)

print(tree.is_balanced())  

    
