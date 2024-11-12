class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = dict()
        for index in range(len(nums)):
            if (target - nums[index]) in record.keys():
                result = []
                result.append(index)
                result.append(record.get(target - nums[index], 0))
                return result
            else:
                record[nums[index]] = index