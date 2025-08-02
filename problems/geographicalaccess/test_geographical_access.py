from geographical_access import GeographicalAccess, TreeNode, GeoNode
import pytest
from typing import List, Tuple


@pytest.fixture
def geo_access() -> GeographicalAccess:
    geo_tree = TreeNode(
        data="world",
        children=[
            TreeNode(
                data="europe",
                children=[
                    TreeNode(data="france", children=[TreeNode(data="paris")]),
                    TreeNode(
                        data="germany",
                        children=[TreeNode(data="munich"), TreeNode(data="berlin")],
                    ),
                ],
            )
        ],
    )
    return GeographicalAccess(geo_tree)


@pytest.mark.parametrize(
    "access_history, check_access, expected",
    [
        ([("1", "paris", "grant")], ("1", "paris"), True),
        ([("1", "munich", "grant")], ("2", "munich"), False),
        ([("1", "munich", "grant"), ("1", "berlin", "grant")], ("1", "berlin"), True),
        ([("1", "paris", "revoke")], ("1", "paris"), False),
        ([("1", "munich", "grant"), ("1", "munich", "revoke")], ("1", "munich"), False),
        ([("1", "munich", "grant"), ("1", "berlin", "revoke")], ("1", "berlin"), False),
        ([("1", "paris", "grant"), ("1", "france", "revoke")], ("1", "paris"), False),
        ([("1", "paris", "revoke"), ("1", "france", "grant")], ("1", "paris"), True),
    ],
)
def test_geographical_access(
    geo_access: GeographicalAccess,
    access_history: List[Tuple[str, str, str]],
    check_access: Tuple[str, str],
    expected: bool,
):
    for access in access_history:
        if access[2] == "grant":
            geo_access.grant_access(access[0], access[1])
        else:
            geo_access.revoke_access(access[0], access[1])
    assert geo_access.check_access(check_access[0], check_access[1]) == expected
