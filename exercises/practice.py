"""Practicing alternatives."""


def short_words(word: list[str]) -> list[str]:
    """Only have short words"""
    i: int = 0
    short_list: list[str] = []
    while i < len(word):
        if len(word[i]) > 5:
            print(f"{word[i]} is too long!")
        else:
            short_list.append(word[i])
    return short_list


print(short_words)
