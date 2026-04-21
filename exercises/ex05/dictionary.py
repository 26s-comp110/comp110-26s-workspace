"""Dictionary Utils."""

__author__: str = "730926082"


def invert(before_invert_dict: dict[str, str]) -> dict[str, str]:
    """Invert the key and value."""
    # Create blank list to place inverted values
    inverted: dict[str, str] = {}
    for elem in before_invert_dict:
        value: str = before_invert_dict[elem]
        if value in inverted:
            raise KeyError("Remember that keys in a dictionary are unique!")
        inverted[value] = elem
    return inverted


def favorite_color(colors: dict[str, str]) -> str:
    """State the most popular color."""
    count: dict[str, int] = {}
    most_popular_color: str = ""
    highest_count: int = 0
    for individual in colors:
        color = colors[individual]
        # Not first time showing up (add to count)
        if color in count:
            count[color] += 1
        # First time showing up (add to list)
        else:
            count[color] = 1
    for color in count:
        if count[color] > highest_count:
            highest_count = count[color]
            most_popular_color = color
    return most_popular_color


def count(list_of_vals_to_count_freq_of: list[str]) -> dict[str, int]:
    """Count how many times a value appeared in the input list."""
    end: dict[str, int] = {}
    for item in list_of_vals_to_count_freq_of:
        if item in end:
            end[item] += 1
        else:
            end[item] = 1
    return end


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Sort words by the first letter."""
    end: dict[str, list[str]] = {}
    for word in words:
        # lowercase so program no confuse same letter bc UPPERCASE
        first = word[0].lower()
        if first.isalpha():
            if first in end:
                end[first].append(word)
            else:
                end[first] = [word]
    return end


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Update the attendance for students for the day."""
    if day in attendance:
        if student not in attendance[day]:  # Avoid adding duplicates
            attendance[day].append(student)
    else:
        attendance[day] = [student]