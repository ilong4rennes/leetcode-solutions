class Solution:
    def calculate_distance(self, x, y):
        return x ** 2 + y ** 2

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        allPoints = []
        for point in points:
            x, y = point[0], point[1]
            allPoints.append((self.calculate_distance(x, y), point))
        allPoints.sort(key = lambda point : point[0])
        results = [allPoints[id][1] for id in range(k)]
        return results