"""
utility collections

frequencies(): takes list of strings as an input and returns dictionary containing the elements frequencies

dedupe(): takes list of strings as an input and returns a list of unique elements in the given list

groupby(): takes list of dictionary and a string key as input and returns a dict mapping key values ot list of items

"""


def frequencies(items: list[str]) -> dict[str, int]:
    """
    - Input: list of strings
    - Output: dict mapping item -> count
    - Example: ["a","b","a"] -> {"a": 2, "b": 1}
    """

    return {i: items.count(i) for i in items}


print(frequencies(["a", "b", "b"]))
print("\n")


def dedupe(items: list[str]) -> list[str]:
    """
    - Input: list with duplicates
     - Output: list preserving first occurrence order
     - Example: ["a","b","a"] -> ["a","b"]
    """

    return list(set(items))


print(dedupe(["a", "b", "b"]))
print("\n")
