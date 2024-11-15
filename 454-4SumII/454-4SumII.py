class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        cnt = {}
        result = 0
        for num1 in nums1:
            for num2 in nums2:
                twosum = num1 + num2
                cnt[twosum] = cnt.get(twosum, 0) + 1
        
        for num3 in nums3:
            for num4 in nums4:
                negtwosum = - (num3 + num4)
                if negtwosum in cnt:
                    result += cnt[negtwosum]
        
        return result