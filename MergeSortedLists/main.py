from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        if list1 == None and list2 == None:
            return []

        if list1 == None:
            return list2

        if list2 == None:
            return list1

        res = []
        head = list1
        while head != None:
            res.append(head.val)
            head = head.next

        head = list2
        while head != None:
            res.append(head.val)
            head = head.next

        res.sort()

        newhead = ListNode(res[0])
        ptr = newhead
        for item in res[1:]:
            ptr.next = ListNode(item)
            ptr = ptr.next

        return newhead


sol = Solution()

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

sol.mergeTwoLists(list1, list2)
