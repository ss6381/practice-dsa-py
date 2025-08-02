# Meta online assessment on CodeSignal.

from collections import defaultdict


class InMemoryDb:
    def __init__(self):
        self.db = defaultdict(list)

    def set(self, timestamp: int, key: str, field: str, value: str) -> None:
        self.db[key].append({"field": field, "value": value})

    def set_with_ttl(
        self, timestamp: int, key: str, field: str, value: str, ttl: int
    ) -> None:
        self.db[key].append({"field": field, "value": value, "ttl": timestamp + ttl})

    def compare_and_set(
        self, timestamp: int, key: str, field: str, expected_value: str, new_value: str
    ) -> bool:
        for item in self.db.get(key, []):
            if item["field"] == field:
                if item["value"] == expected_value:
                    item["value"] = new_value
                    return True
        return False

    def compare_and_set_with_ttl(
        self,
        timestamp: int,
        key: str,
        field: str,
        expected_value: str,
        new_value: str,
        ttl: int,
    ) -> bool:
        for item in self.db.get(key, []):
            if item["field"] == field:
                if item["value"] == expected_value:
                    item["value"] = new_value
                    item["ttl"] = timestamp + ttl
                    return True
        return False

    def delete(self, key: str, field: str) -> bool:
        for item in self.db.get(key, []):
            if item["field"] == field:
                self.db[key].remove(item)
                return True
        return False

    def get(self, timestamp: int, key: str, field: str) -> str:
        for item in self.db.get(key, []):
            if item["field"] == field:
                if "ttl" in item and item["ttl"] < timestamp:
                    return item["value"]
                return item["value"]
        return None

    def scan(self, key: str) -> list[str]:
        result = []
        sorted_items = sorted(self.db.get(key, []), key=lambda x: x["field"])
        for item in sorted_items:
            result.append(f"{item['field']}({item['value']})")
        return result

    def scan_by_prefix(self, key: str, prefix: str) -> list[str]:
        result = []
        sorted_items = sorted(self.db.get(key, []), key=lambda x: x["field"])
        for item in sorted_items:
            if item["field"].startswith(prefix):
                result.append(f"{item['field']}({item['value']})")
        return result
