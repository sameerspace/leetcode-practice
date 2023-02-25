from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid = head
        ptr = head
        while ptr.next != None:
            mid = mid.next
            if ptr.next.next == None:
                return mid
            ptr = ptr.next.next
        return mid
