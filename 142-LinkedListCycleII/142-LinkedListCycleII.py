# Last updated: 5/17/2025, 6:49:10 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow: break
        if fast == None or fast.next == None: return None
        slow = head
        while fast != slow:
            slow = slow.next
            fast = fast.next
        return slow