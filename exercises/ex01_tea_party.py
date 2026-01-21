"""Plan a cozy tea party and practice COMP 110 concepts."""

__author__: str = "730738394"


"""Entrypoint of the program"""


def main_planner(guests: int) -> None:
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))
    return None


# I had the most difficulty with these print functions.
# I went to office hours for this issue
# and the ULA told me that I needed to include the print functions indented
# under the main_planner definition, which I had not done.
# He also helped me correct the text within the str() part.


def tea_bags(people: int) -> int:
    return int(people * 2)


"""Define tea bags and indicate that there are two tea bags for every one attendee."""


def treats(people: int) -> int:
    return int(tea_bags(people) * 1.5)


# argument
# I struggled with the return function above.
# I did not realize I had to add "(people)" for some time.

"""Define treats and establish that each person gets 1.5 treats for every tea bag they use."""


def cost(tea_count: int, treat_count: int) -> float:
    total_cost = float(tea_count * 0.5) + (treat_count * 0.75)
    return total_cost


# I also ran into many errors during this cost part.
# Particularly, the program didn't like me trying to add
# the int parameters tea_bag and treats in a float return statement.
# In the end, I looked back at prior practice from class to
# get a sense of what I needed to add and change.

"""Define cost for each tea bag and treat."""

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
