class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        result = 0 
        for char in stones:
            if char in jewels:
                result += 1
        return result