# Last updated: 5/20/2025, 2:08:30 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        p = dummy
        pq = []
        heapq.heapify(pq)
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(pq, (node.val, i, node))
        while pq:
            minVal, i, node = heapq.heappop(pq)
            p.next = node
            p = p.next
            if node.next:
                heapq.heappush(pq, (node.next.val, i, node.next))
        return dummy.next