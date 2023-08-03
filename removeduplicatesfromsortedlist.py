#https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/
#Remove Duplicates from Sorted List
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def remove_duplicates_sorted_list(lst):
    if not lst:
        return []

    unique_list = [lst[0]]

    for i in range(1, len(lst)):
        if lst[i] != lst[i - 1]:
            unique_list.append(lst[i])

    return unique_list


sorted_list = [1, 1, 2]
result = remove_duplicates_sorted_list(sorted_list)
print(result)  # Output: [1, 2, 3, 4, 5, 6]


