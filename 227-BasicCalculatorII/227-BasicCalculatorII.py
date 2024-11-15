class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        stack = []
        op = '+'
        s = s.replace(" ", "")

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            if not char.isdigit() or i == len(s) - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    last_num = stack.pop()
                    stack.append(last_num * num)
                elif op == '/':
                    last_num = stack.pop()
                    stack.append(int(last_num / num))
                op = char
                num = 0
        return sum(stack)