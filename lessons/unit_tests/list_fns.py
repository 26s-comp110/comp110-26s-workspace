"""Unit tests"""


def get_first(input_list: list[str]) -> str:
    """Get the first elem."""
    if len(input_list) == 0:
        return ""
    else:
        return input_list[0]


def remove_first(input_list: list[str]) -> None:
    """Remove the first elem."""
    if len(input_list) != 0:
        input_list.pop(0)


def get_and_remove_first(input_list: list[str]) -> str:
    """Get and remove the first elem."""
    # Whatever it pops it also returns it! hehhhehe
    return input_list.pop(0)


a: list[str] = ["a", "b"]
print(get_first(a))
