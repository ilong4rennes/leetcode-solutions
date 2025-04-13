# Last updated: 4/13/2025, 4:32:12 PM
class Codec:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for string in strs:
            result += str(len(string)) + '#' + string
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        while s != '':
            sepPos = s.index('#')
            length = s[:sepPos]
            result, s = self.getStr(length, s, result)
        return result
    
    def getStr(self, length, s, result):
        startPos = len(length) + 1
        length = int(length)
        endPos = startPos + length
        string = s[startPos:endPos]
        result.append(string)
        s = s[endPos:]
        return result, s
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))