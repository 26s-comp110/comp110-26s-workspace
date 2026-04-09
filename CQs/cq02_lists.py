"""Mutating functions."""

__author__: str = "730926082"


def manual_append(idk: list[int], idk_w: int) -> None:
    idk.append(idk_w)


def double(list: list[int]) -> None:
    i: int = 0
    while i <= (len(list) - 1):
        if list[i] > 0:  # if the num is 0 then multiplying it wouldn't matter
            list[i] = list[i] * 2  # change whatever i is there by *2
        i += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
