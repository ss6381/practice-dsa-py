from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Employee:
    eid: str
    reports: List[Optional["Employee"]]


class Organization:

    def __init__(self):
        self.employees: List[Employee] = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def generate_org_chart(self) -> List[Employee]:
        pass
