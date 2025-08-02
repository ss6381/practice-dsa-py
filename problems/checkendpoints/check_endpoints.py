"""
Questions: 
Examples: 
Algorithm: 
Data structures: 
Tradeoffs: 
Time/Space complexity: 
"""

from requests import get, Response
from collections import deque
from typing import Dict, List, Optional

BASE_URL = "https://beliefs-poison-peaceful-sur.trycloudflare.com"


def find_congrats(step_id: str = "") -> Optional[str]:
    q = deque([step_id])
    while q:
        curr_step_id = q.popleft()
        response: Response = retry(url="/".join([BASE_URL, curr_step_id]))
        response_json: Dict[str, List[str]] = response.json()
        if "message" in response_json.keys() and response_json["message"] == "CONGRATS":
            return curr_step_id
        for next_step_id in response_json["next_steps"]:
            q.append(next_step_id)
    return None


def retry(url: str) -> Response:
    retry = 5  # would read this from environment or config file
    for _ in range(retry):
        response: Response = get(url)
        if response.status_code == 200:
            return response
    response.raise_for_status()


result = find_congrats()
print(result)
""" OUTPUT:

{'next_steps': ['XCMGOOAFHX', 'TEUDQDAWFF']}
XCMGOOAFHX
{'next_steps': ['ZWHYORFYRZ', 'XHJEDBHPAR', 'IIVMIMSBZA']}
TEUDQDAWFF
{'next_steps': ['ZWHYORFYRZ', 'XHJEDBHPAR', 'IIVMIMSBZA']}
ZWHYORFYRZ
{'next_steps': ['TVAUJPABEY', 'FTYYIJNUCT']}
XHJEDBHPAR
{'next_steps': ['FTYYIJNUCT', 'UWAYCIPXIY']}
IIVMIMSBZA
{'next_steps': ['UWAYCIPXIY', 'OIIECDRZEB']}
ZWHYORFYRZ
{'next_steps': ['TVAUJPABEY', 'FTYYIJNUCT']}
XHJEDBHPAR
{'next_steps': ['FTYYIJNUCT', 'UWAYCIPXIY']}
IIVMIMSBZA
{'next_steps': ['UWAYCIPXIY', 'OIIECDRZEB']}
TVAUJPABEY
{'next_steps': ['ZNKGPVLKBX']}
FTYYIJNUCT
{'next_steps': ['MHKDJZYQMI', 'AOGRMVQUJQ', 'JSHMURHYQP']}
FTYYIJNUCT
{'next_steps': ['MHKDJZYQMI', 'AOGRMVQUJQ', 'JSHMURHYQP']}
UWAYCIPXIY
{'next_steps': ['HKCVJAPCOI', 'PYVKVQJDPO', 'YZPJXACOPD']}
UWAYCIPXIY
{'next_steps': ['HKCVJAPCOI', 'PYVKVQJDPO', 'YZPJXACOPD']}
OIIECDRZEB
{'next_steps': ['QXJLFHZJYX']}
TVAUJPABEY
{'next_steps': ['ZNKGPVLKBX']}
FTYYIJNUCT
{'next_steps': ['MHKDJZYQMI', 'AOGRMVQUJQ', 'JSHMURHYQP']}
FTYYIJNUCT
{'next_steps': ['MHKDJZYQMI', 'AOGRMVQUJQ', 'JSHMURHYQP']}
UWAYCIPXIY
{'next_steps': ['HKCVJAPCOI', 'PYVKVQJDPO', 'YZPJXACOPD']}
UWAYCIPXIY
{'next_steps': ['HKCVJAPCOI', 'PYVKVQJDPO', 'YZPJXACOPD']}
OIIECDRZEB
{'next_steps': ['QXJLFHZJYX']}
ZNKGPVLKBX
{'next_steps': ['AMVDTYQUCL']}
MHKDJZYQMI
{'next_steps': ['CHUWJUUSRT']}
AOGRMVQUJQ
{'next_steps': []}
JSHMURHYQP
{'next_steps': ['EVYMRSSEUP']}
MHKDJZYQMI
{'next_steps': ['CHUWJUUSRT']}
AOGRMVQUJQ
{'next_steps': []}
JSHMURHYQP
{'next_steps': ['EVYMRSSEUP']}
HKCVJAPCOI
{'next_steps': []}
PYVKVQJDPO
{'next_steps': []}
YZPJXACOPD
{'next_steps': []}
HKCVJAPCOI
{'next_steps': []}
PYVKVQJDPO
{'next_steps': []}
YZPJXACOPD
{'next_steps': []}
QXJLFHZJYX
{'next_steps': ['PGZMKIZMHM']}
ZNKGPVLKBX
{'next_steps': ['AMVDTYQUCL']}
MHKDJZYQMI
{'next_steps': ['CHUWJUUSRT']}
AOGRMVQUJQ
{'next_steps': []}
JSHMURHYQP
{'next_steps': ['EVYMRSSEUP']}
MHKDJZYQMI
{'next_steps': ['CHUWJUUSRT']}
AOGRMVQUJQ
{'next_steps': []}
JSHMURHYQP
{'next_steps': ['EVYMRSSEUP']}
HKCVJAPCOI
{'next_steps': []}
PYVKVQJDPO
{'next_steps': []}
YZPJXACOPD
{'next_steps': []}
HKCVJAPCOI
{'next_steps': []}
PYVKVQJDPO
{'next_steps': []}
YZPJXACOPD
{'next_steps': []}
QXJLFHZJYX
{'next_steps': ['PGZMKIZMHM']}
AMVDTYQUCL
{'next_steps': ['DVHLZWZLMS']}
CHUWJUUSRT
{'next_steps': ['EVYMRSSEUP']}
EVYMRSSEUP
{'message': 'CONGRATS'}
EVYMRSSEUP
"""
