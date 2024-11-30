class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = len(nums)
        return self.mergeSort(nums, start, end)

    def mergeSort(self, nums, start, end):
        if end - start <= 1: return
        mid = (start + end) // 2
        self.mergeSort(nums, start, mid)
        self.mergeSort(nums, mid, end)
        self.merge(nums, start, mid, end)
    
    def merge(self, nums, start, mid, end):
        left = nums[start:mid]
        right = nums[mid:end]
        i = j = 0
        k = start 

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else: 
                nums[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
        