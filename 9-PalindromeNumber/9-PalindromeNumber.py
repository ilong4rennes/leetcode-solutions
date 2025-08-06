# Last updated: 8/5/2025, 8:29:45 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if the number is negative, we should return False
        if x < 0: return False
        
        # Turn int into str first
        x_str = str(x) # O(N)
        
        # Initialize two pointers, left -> first number index, right -> last number index
        left, right = 0, len(x_str) - 1
        
        # loop: if left_num != right_num: return False
        while left < right: # O(log N)
            left_num, right_num = x_str[left], x_str[right]
            if left_num != right_num: 
                return False
            left += 1
            right -= 1
            
        # return True
        return True