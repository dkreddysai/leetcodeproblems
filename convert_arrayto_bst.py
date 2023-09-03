from typing import List
from queue import Queue

# structure of the tree node


class Node:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

# function to convert the array to BST
# and return the root of the created tree


def sortedArrayToBST(nums: List[int]) -> Node:
	# if the array is empty return None
	if not nums:
		return None

	n = len(nums)
	mid = n // 2
	root = Node(nums[mid])
	# initializing queue
	q = Queue()
	# push the root and its indices to the queue
	q.put((root, (0, mid-1)))
	q.put((root, (mid+1, n-1)))

	while not q.empty():
		# get the front element from the queue
		curr = q.get()

		# get the parent node and its indices
		parent = curr[0]
		left = curr[1][0]
		right = curr[1][1]

		# if there are elements to process and parent node is not None
		if left <= right and parent is not None:
			mid = (left + right) // 2
			child = Node(nums[mid])

			# set the child node as left or right child of the parent node
			if nums[mid] < parent.val:
				parent.left = child
			else:
				parent.right = child

			# push the left and right child and their indices to the queue
			q.put((child, (left, mid-1)))
			q.put((child, (mid+1, right)))

	return root

# function to print the preorder traversal
# of the constructed BST


def printBST(root: Node) -> None:
	if root is None:
		return

	print(root.val, end=" ")
	printBST(root.left)
	printBST(root.right)


# Driver program to test the above function
if __name__ == "__main__":
	# create a sorted array
	nums = [1, 2, 3, 4, 5, 6, 7]
	root = sortedArrayToBST(nums)
	printBST(root)
