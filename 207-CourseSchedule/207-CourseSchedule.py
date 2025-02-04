class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Build graph & in-degree array
        graph = defaultdict(list)
        # key = prereq, value = courses unlocked by prereq
        in_degree = [0] * numCourses
        # id = course, val = # of in-degree
        for relation in prerequisites:
            course, prereq = relation[0], relation[1]
            graph[prereq].append(course)
            in_degree[course] += 1

        # 2. Initialize queue
        queue = deque()
        for course in range(len(in_degree)):
            if in_degree[course] == 0:
                queue.append(course)
        
        # 3. Process node with 0 in-degree 
        count = 0
        while queue:
            course = queue.pop()
            count += 1
            # loop through all the unlocked courses
            for next_course in graph[course]:
                # update in_degree of next_course
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        # 4. Final check
        return count == numCourses