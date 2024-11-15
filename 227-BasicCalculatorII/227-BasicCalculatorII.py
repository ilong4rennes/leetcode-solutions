class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        op = '+'
        s = s.replace(" ", "")  # Remove spaces for simplicity
        
        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)  # Handle multi-digit numbers
            
            if not char.isdigit() or i == len(s) - 1:
                # Process the operator
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    # Use int to truncate toward zero
                    stack.append(int(stack.pop() / num))
                
                # Update operator and reset number
                op = char
                num = 0
        
        return sum(stack)