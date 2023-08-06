#https://leetcode.com/problems/same-tree/submissions/
# Same Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#https://leetcode.com/problems/same-tree/submissions/
# Same Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
def newNode(data):
    node = Node(data)
    return node
def isSameStructure(a, b):
 
    
    if (a == None and b == None):
        return 1;
  

    if (a != None and b != None):
     
        return (
            isSameStructure(a.left, b.left) and
            isSameStructure(a.right, b.right))
         
    
    return 0;

if __name__=='__main__':
     
    root1 = newNode(1);
    root2 = newNode(1);
    root1.left = newNode(2);
    root1.right = newNode(3);
   
  
    root2.left = newNode(2);
    root2.right = newNode(3);
    
    if (isSameStructure(root1, root2)):
        print("Both trees have same structure");
    else:
        print("Trees do not have same structure");
        
