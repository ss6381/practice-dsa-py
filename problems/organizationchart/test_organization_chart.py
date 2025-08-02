from organization_chart import Employee, Organization
import pytest
from typing import List


@pytest.fixture
def org():
    return Organization()


@pytest.mark.parametrize("employees, expected", [()])
def test_generate_org_chart(
    org: Organization, employees: List[Employee], expected: List[Employee]
):
    for employee in employees:
        org.add_employee(employee)
    assert org.generate_org_chart() == expected
