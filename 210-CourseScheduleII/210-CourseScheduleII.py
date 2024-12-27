class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 1. Build graph & in-degree array
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        result = []
        for relation in prerequisites:
            course, prereq = relation[0], relation[1]
            graph[prereq].append(course)
            in_degree[course] += 1
        
        # 2. Initialize queue
        queue = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.appendleft(course)

        # 3. Process nodes with 0 in-degree
        while queue:
            course = queue.pop()
            result.append(course)
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.appendleft(next_course)
        if len(result) != numCourses:  
            return []
        return result