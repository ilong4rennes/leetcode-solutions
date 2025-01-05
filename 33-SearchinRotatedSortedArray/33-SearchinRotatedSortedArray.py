class Solution:
   def search(self, nums: List[int], target: int) -> int:
       n = len(nums)
       left, right = 0, n - 1
       
       # Find the index of the pivot element (the smallest element)
       while left <= right:
           mid = (left + right) // 2
           if nums[mid] > nums[-1]:
               left = mid + 1
           else:
               right = mid - 1
       
       # Shift elements in circular manner, with the pivot element at index 0.
       # Then perform a regular binary search
       def shiftedBinarySearch(pivot_index, target):
           left, right = 0, n - 1

           while left <= right:
               mid = (left + right) // 2
               if nums[(mid + pivot_index) % n] == target:
                   return (mid + pivot_index) % n
               elif nums[(mid + pivot_index) % n] > target:
                   right = mid - 1
               else:
                   left = mid + 1
           return -1
           
       return shiftedBinarySearch(left, target)