# Last updated: 11/12/2025, 11:18:34 AM
class Solution:
    def reverseWords(self, s: str) -> str:
        sb = []
        # 先清洗一下数据，把多于的空格都删掉
        for c in s:
            if c != ' ':
                # 单词中的字母/数字
                sb.append(c)
            elif sb and sb[-1] != ' ':
                # 单词之间保留一个空格
                sb.append(' ')
        if not sb:
            return ""
        # 末尾如果有空格，清除之
        if sb[-1] == ' ':
            sb.pop()

        # 清洗之后的字符串
        chars = list(''.join(sb))
        n = len(chars)
        # 进行单词的翻转，先整体翻转
        self.reverse(chars, 0, n - 1)
        # 再把每个单词翻转
        i = 0
        while i < n:
            for j in range(i, n):
                if j + 1 == n or chars[j + 1] == ' ':
                    # chars[i..j] 是一个单词，翻转之
                    self.reverse(chars, i, j)
                    # 把 i 置为下一个单词的首字母
                    i = j + 2
                    break
        
        # 最后得到题目想要的结果
        return ''.join(chars)

    # 翻转 arr[i..j]
    def reverse(self, arr, i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1