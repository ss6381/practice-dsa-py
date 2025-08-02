from collections import defaultdict


def course_schedule(prerequisites: list[tuple[int, int]]) -> bool:
    # convert prerequisites to adjacency list
    graph: dict[int, list[int]] = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    # get all unique courses
    all_courses = set()
    for course, prereq in prerequisites:
        all_courses.add(course)
        all_courses.add(prereq)

    visited = set()
    cycles = set()  # recursion stack for cycle detection

    def has_cycle(node: int) -> bool:
        if node in cycles:
            return True  # cycle detected
        if node in visited:
            return False
        visited.add(node)
        cycles.add(node)

        for neighbor in graph[node]:
            if has_cycle(neighbor):
                return True
        cycles.remove(node)
        return False

    for course in all_courses:  # check each course for cycles
        if course not in visited:
            if has_cycle(course):
                return False  # cycle found, impossible to complete
    return True  # no cycles found, possible to complete
