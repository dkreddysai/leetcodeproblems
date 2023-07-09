def mergeTwoLists(self, list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    curr = dummy = ListNode()
    while list1 and list2:
        if list1.val>list2.val:
            curr.next=list2
            list2=list2.next
        else:
            curr.next=list1
            list1=list1.next
        curr = curr.next
    if not list1:
        curr.next = list2
    else:
        curr.next=list1
    return dummy.next
list1=[1,2,4,5,6]
list2=[1,2,4,3]
print(sorted(list1+list2))
            
