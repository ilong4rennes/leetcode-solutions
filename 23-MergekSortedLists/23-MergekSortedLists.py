# Last updated: 10/8/2025, 7:11:30 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None
        return self.mergeKLists3(lists, 0, len(lists) - 1)
    
    def mergeKLists3(self, lists, start, end):
        if start == end: return lists[start]
        mid = start + (end - start) // 2
        left = self.mergeKLists3(lists, start, mid)
        right = self.mergeKLists3(lists, mid + 1, end)
        return self.merge2Lists(left, right)
        
    def merge2Lists(self, list1, list2):
        p = dummy = ListNode(-1)
        p1 = list1
        p2 = list2
        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        if p1: p.next = p1
        if p2: p.next = p2
        return dummy.next