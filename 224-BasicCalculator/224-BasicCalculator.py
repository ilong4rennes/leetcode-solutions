class Solution:
    def calculate(self, s: str) -> int:
        result, num, sign = self.initialize()
        stack = []

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '+':
                result += num * sign
                sign = 1
                num = 0
            elif char == '-':
                result += num * sign
                sign = -1
                num = 0
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result, num, sign = self.initialize()
            elif char == ')':
                result += num * sign
                num = 0
                sign = stack.pop()
                prev_num = stack.pop()
                result = prev_num + result * sign
        result += num * sign
        return result
        
    def initialize(self):
        result = 0
        num = 0
        sign = 1
        return result, num, sign
