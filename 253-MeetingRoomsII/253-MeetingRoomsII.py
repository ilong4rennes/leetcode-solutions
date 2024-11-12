class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        intervals.sort()
        for (start, end) in intervals:
            if heap == [] or start < heap[0]:
                heapq.heappush(heap, end)
            else:
                heapq.heappushpop(heap, end)
        return len(heap)