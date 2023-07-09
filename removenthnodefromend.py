class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy

    for i in range(n + 1):
        second = second.next
    while second is not None:
        first = first.next
        second = second.next
    first.next = first.next.next
    return dummy.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

n = 2

new_head =removeNthFromEnd(head, n)

current = new_head
while current is not None:
    print(current.val)
    current = current.next
