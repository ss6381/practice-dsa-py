# # Brex - Phone screen on 6/25/2025
# # Topological sort


# class Task:
#     def __init__(self, key, dependencies=[]):
#         self.key = key
#         self.dependencies = dependencies

#     def __repr__(self):
#         return self.key


# # brainstorm
# # coffee, toast
# # yoga


# class TaskScheduler:
#     def __init__(self):
#         self.tasks = []

#     def print(self):
#         print(self.tasks)

#     def add_task(self, task) -> bool:
#         self.tasks.append(task)

#     def complete_task(self, task) -> bool:
#         if task not in self.tasks:
#             raise ValueError("Error: Task not found in scheduled tasks.")
#         self.tasks.remove(task)

#     def get_next_task(self):
#         if len(self.tasks) <= 0:
#             return None

#         # task 1, deps: 2, 3
#         # task 2, deps: 3
#         # 1, 2, 3, 4
#         for task in self.tasks:
#             task_found = True
#             for dep in task.dependencies:
#                 if dep in self.tasks:
#                     task_found = False
#             if task_found:
#                 return task
#         return None

#     def get_completion_plan_for(self, task):
#         return self.get_completion_plan_for_helper(task)

#     def get_completion_plan_for_helper(self, task, result=[], seen=set()):
#         # post order traversal
#         if len(task.dependencies) == 0:
#             result.append(task)
#             return result

#         for dep in task.dependencies:
#             if dep not in seen:
#                 seen.add(dep)
#                 self.get_completion_plan_for_helper(dep, result, seen)

#         result.append(task)
#         return result


# def test1():
#     print("--- TEST 1 ---")
#     scheduler = TaskScheduler()
#     coffee_task = Task("Brew some coffee")
#     scheduler.print()
#     scheduler.add_task(coffee_task)
#     scheduler.print()
#     cookie_task = Task("Eat a cookie")
#     scheduler.add_task(cookie_task)
#     scheduler.print()
#     next_task = scheduler.get_next_task()
#     # Should be coffee_task
#     scheduler.complete_task(next_task)
#     next_task = scheduler.get_next_task()
#     # Should be cookie_task
#     scheduler.print()


# def test2():
#     print("--- TEST 2 ---")
#     scheduler = TaskScheduler()
#     coffee_task = Task("Brew some coffee")
#     toast_task = Task("Make a toast")
#     brainstorm_task = Task("Brainstorm project ideas", [coffee_task, toast_task])
#     scheduler.add_task(brainstorm_task)
#     scheduler.add_task(coffee_task)
#     scheduler.add_task(toast_task)
#     scheduler.print()
#     next_task = scheduler.get_next_task()  # Should be coffee_task or toast_task
#     scheduler.complete_task(next_task)
#     scheduler.print()
#     next_task = scheduler.get_next_task()  # Should be coffee_task or toast_task
#     scheduler.complete_task(next_task)
#     scheduler.print()
#     next_task = scheduler.get_next_task()  # Should be brainstorm_task
#     scheduler.complete_task(next_task)
#     scheduler.print()


# def test3():
#     print("--- TEST 3 ---")
#     scheduler = TaskScheduler()
#     yoga_task = Task("Do yoga")
#     coffee_task = Task("Brew some coffee", [yoga_task])
#     toast_task = Task("Make a toast", [yoga_task])
#     brainstorm_task = Task("Brainstorm project ideas", [coffee_task, toast_task])
#     scheduler.add_task(yoga_task)
#     scheduler.add_task(brainstorm_task)
#     scheduler.add_task(toast_task)
#     scheduler.add_task(coffee_task)
#     scheduler.print()
#     completion_plan = scheduler.get_completion_plan_for(brainstorm_task)
#     # Should be Do yoga, Brew some coffee / Make a toast, Brainstorm project ideas.
#     print("completion_plan:", completion_plan)


# if __name__ == "__main__":
#     test3()
#     test2()
#     test1()


from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Task:
    key: str
    deps: List[Optional["Task"]]

    def __str__(self):
        return f"key: {self.key}"


class TaskScheduler:
    def __init__(self):
        self.tasks: List[Optional[Task]] = []

    def add_task(self, key: str) -> Task:
        pass

    def complete_task(self, task: Task) -> bool:
        pass

    def get_next_task(self) -> Task:
        pass

    def completion_plan(self, task: Task) -> str:
        pass
