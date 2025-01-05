# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1: return 1
        low, high = 1, n 
        while low <= high:
            mid = (low + high) // 2
            if isBadVersion(mid) == True:
                high = mid - 1
                if mid == 0 or isBadVersion(mid - 1) == False:
                    return mid 
            else:
                low = mid + 1