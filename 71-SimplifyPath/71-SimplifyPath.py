# Last updated: 10/9/2025, 3:39:50 AM
class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        stack = []
        for part in parts:
            if part == '' or part == '.':
                continue
            elif part == '..':
                if stack:
                    stack.pop()
                continue
            else:
                stack.append(part)
        result = ''
        while stack:
            currDir = stack.pop()
            result = '/' + currDir + result
        return result if result else '/'