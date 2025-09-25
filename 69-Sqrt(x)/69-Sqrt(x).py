# Last updated: 9/25/2025, 2:28:31 AM
class Solution:
    def mySqrt(self, x: int) -> int:
        root = 1
        while (x - root ** 2) >= 0:
            root += 1
        return root - 1