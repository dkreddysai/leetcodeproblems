class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 or l2:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

        current = current.next

    if carry > 0:
        current.next = ListNode(carry)

    return dummy.next
# Example usage:
# l1: 2 -> 4 -> 3 (represents the number 342)
# l2: 5 -> 6 -> 4 (represents the number 465)
# Sum: 807
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

result = addTwoNumbers(l1, l2)
while result:
    print(result.val, end=' ')
    result = result.next

