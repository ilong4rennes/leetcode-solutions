from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordsCounter = Counter(words)
        wordsHeap = []
        for word, freq in wordsCounter.items():
            heappush(wordsHeap, (-freq, word))
            
        res = []
        for _ in range(k):
            res.append(heapq.heappop(wordsHeap)[1])
            
        return res