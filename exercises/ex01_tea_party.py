"""Tea Party Assignment"""

__author__: str = "730926082"


def main_planner(guests: int) -> None:
    """Bringing all the functions together."""
    print("A Cozy Tea Party for", guests, "People!")
    # It's important to mark spaces to make optimal copy
    print("Tea Bags:", tea_bags(people=guests))
    print("Treats:", treats(people=guests))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))
    # I was setting it equal to guests


def tea_bags(people: int) -> int:
    """Number of Tea Bags for Guests"""
    return people * 2


def treats(people: int) -> int:
    """ "Number of treats for guests"""
    return int(tea_bags(people=people) * 1.5)


# int does not need to be in two different lines. This gets it done in one


def cost(tea_count: int, treat_count: int) -> float:
    """ "Cost of the tea bags and treats"""
    return tea_count * 0.50 + treat_count * 0.75


# I dont believe parenthesis are needed here


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
