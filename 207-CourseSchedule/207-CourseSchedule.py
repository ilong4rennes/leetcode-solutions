class Solution:
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Build the graph and in-degree array
        graph = [[] for _ in range(num_courses)]
        in_degree = [0] * num_courses
        for relation in prerequisites:
            graph[relation[1]].append(relation[0])  # Edge from prerequisite to course
            in_degree[relation[0]] += 1

        # Step 2: Initialize a queue with courses of zero in-degree
        queue = deque()
        for course, degree in enumerate(in_degree):
            if degree == 0:
                queue.appendleft(course)

        # Step 3: Process zero in-degree courses
        count = 0  # Count of processed courses
        while queue:
            course = queue.pop()
            count += 1
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.appendleft(next_course)

        # Step 4: Check if all courses are processed
        return count == num_courses