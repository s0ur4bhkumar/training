# 1. `invert_dict(d: dict[str, str]) -> dict[str, str]` - swap keys and values
from typing import Callable


def invert_dict(d: dict[str, str]) -> dict[str, str]:
    result: dict[str, str] = {}
    for key, value in d.items():
        result[value] = key
    return result


print(invert_dict({"a": "b", "c": "d", "e": "f"}))

# 2. `merge_dicts(*dicts: dict) -> dict` - merge multiple dicts (later values override)


def merge_dicts(*dicts: dict[str, str]) -> dict[str, str]:
    result: dict[str, str] = {}
    for i in dicts:
        for j in i:
            result[j] = i[j]
    return result


# 3. `filter_dict(d: dict, predicate) -> dict` - keep only items where predicate(key, value) is True


def predicate(x: str | int, y: int) -> bool:
    return x in ["a", "b", "c"]


def filter_dict(
    d: dict[int | str, int], predicate: Callable[[str | int, int], bool]
) -> dict[str | int, int]:
    return {key: value for key, value in d.items() if predicate(key, value)}

print(filter_dict( {'a':'b','c':'d','e':'f'},predicate))

