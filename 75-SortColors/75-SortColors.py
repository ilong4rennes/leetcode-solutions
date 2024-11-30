class Solution:
     def sortColors(self, nums):
        def merge_sort(arr, start, end):
            if end - start <= 1:
                return
            
            mid = (start + end) // 2
            merge_sort(arr, start, mid)
            merge_sort(arr, mid, end)
            merge(arr, start, mid, end)
        
        def merge(arr, start, mid, end):
            left = arr[start:mid]
            right = arr[mid:end]
            i = j = 0
            k = start
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
        
        # Apply merge sort on the entire array
        merge_sort(nums, 0, len(nums))
        