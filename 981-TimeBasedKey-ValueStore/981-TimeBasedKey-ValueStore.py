# Last updated: 4/30/2025, 12:37:05 AM
class TimeMap:

    def __init__(self):
        self.timeDict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeDict[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if not self.timeDict[key]: return ''
        allVals = self.timeDict[key]
        lo, hi = 0, len(allVals) - 1
        result = ''
        while lo <= hi:
            mid = (lo + hi) // 2
            prevTime = allVals[mid][0]
            if prevTime <= timestamp:
                result = allVals[mid][1]
                lo = mid + 1
            else:
                hi = mid - 1
        return result  


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)