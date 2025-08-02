# Bolt - 1st Round
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Merchant:
    key: chr
    capacity: int
    amount: int = 0


def split(accounts: List[Merchant], amount: int) -> List[Tuple[chr, int]]:
    """
    You have a sum of money to distribute among a number of merchant accounts. You need to distribute the money as evenly as possible. But some merchants have a maximum amount they can take. We only deal with dollar amounts, no decimals.

    Amount: $100 --> 90 --> 70
    Accounts: [('a', 20), ('b', 100), ('c', 10), ('d', 100)]
    Result: [('a', 20), ('b', 35), ('c', 10), ('d', 35)]

    10, 90, 0, 90, ($60 left).
     0, 80, 0, 80, ($30 left).
     0, 65, 0, 65, ($0 left).

    Consider: [('c', 80), ('a', 90), ('b', 100), ('d', 100)]

    Amount: $101
    Accounts: [('a', 20), ('b', 100), ('c', 10), ('d', 100)]
    Result: [('a', 20), ('b', 36), ('c', 10), ('d', 35)]

    Amount: $200
    Accounts: [('a', 20), ('b', 110), ('c', 10), ('d', 110), ('e', 100), ('f', 100)]
    Result: [('a', 20), ('b', 35), ('c', 10), ('d', 35), ('e', 35), ('f', 35)]
    """
    n = len(accounts)
    allocations = [0] * n
    remaining = set(range(n))
    remaining_amount = amount
    while remaining and remaining_amount > 0:
        fair_share = remaining_amount // len(remaining)
        if fair_share == 0:
            # Distribute the remaining dollars one by one to the earliest merchants
            for i in sorted(remaining):
                if remaining_amount == 0:
                    break
                give = min(accounts[i].capacity - allocations[i], 1)
                allocations[i] += give
                remaining_amount -= give
                if allocations[i] == accounts[i].capacity:
                    # Remove merchant if at capacity
                    remaining.remove(i)
            break
        to_remove = set()
        for i in remaining:
            can_give = min(fair_share, accounts[i].capacity - allocations[i])
            allocations[i] += can_give
            remaining_amount -= can_give
            if allocations[i] == accounts[i].capacity:
                to_remove.add(i)
        remaining -= to_remove
    return [(accounts[i].key, allocations[i]) for i in range(n)]
