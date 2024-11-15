class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_cnt = {}
        for char in chars:
            char_cnt[char] = char_cnt.get(char, 0) + 1
        
        result = 0
        for word in words:
            temp_cnt = char_cnt.copy()
            is_good_str = True
            for char in word:
                if temp_cnt.get(char, 0) <= 0:
                    is_good_str = False
                    break
                else:
                    temp_cnt[char] -= 1
            if is_good_str: result += len(word)
        return result