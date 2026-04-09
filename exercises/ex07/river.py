"""File to define River class."""

from __future__ import annotations
from ex07.fish import Fish
from ex07.bear import Bear


class River:

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """docstring"""
        i: int = 0
        # As animal’s age, they should be removed from the River. Modify the check_ages
        while len(self.fish) > 0 and self.fish[0].age > 3:
            self.fish.pop(0)
        while len(self.bears) > 0 and self.bears[0].age > 5:
            self.bears.pop(0)
        i += 1
        return None

    def bears_eating(self):
        """docstring"""
        # Modify the bears_eating method, so that, for each Bear, if there are at least
        i: int = 0
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
        i += 1
        return None

    def check_hunger(self):
        """docstring"""
        # If hunger_score < 0, then remove the Bear from the river.
        i: int = 0
        while len(self.bears) > 0 and self.bears[0].hunger_score < 0:
            self.bears.pop(0)
        i += 1
        return None

    def repopulate_fish(self):
        """docstring"""
        i: int = 0
        # for n fish, there will be int(n/2) * 4 new fish added to fish
        while len(self.fish) >= 2 and self.fish[0].age > 1 and self.fish[1].age > 1:
            self.fish.append(Fish())
        i += 1

        return None

    def repopulate_bears(self):
        """docstring"""
        # To generalize, for n bears, there will be int(n/2) new Bears added to bears.
        i: int = 0
        while len(self.bears) >= 2 and self.bears[0].age > 3 and self.bears[1].age > 3:
            self.bears.append(Bear())
        i += 1
        return None

    def __str__(self) -> str:
        """docstring"""
        return (
            "~~~ Day {self.day}: ~~~\n"
            " Fish population: {len(self.fish)}"
            "\n Bear population: "
            "{len(self.bears)}"
        )

    def __add__(self, other_riv: River) -> River:
        """docstring"""
        # modify the __add__method so that it sums the fish and sums the bears in the
        new_fish: int = len(self.fish) + len(other_riv.fish)
        new_bears: int = len(self.bears) + len(other_riv.bears)
        new_river: River = River(new_fish, new_bears)

        return new_river

    def __mul__(self, factor: int) -> River:
        """docstring"""
        new_river: River = River(factor, factor)

        return new_river

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        print(self)

    def one_river_week(self):
        """docstring"""
        # It should simply call one_river_day() seven times
        for _ in range(7):
            self.one_river_day()

    def remove_fish(self, amount: int):
        """docstring"""
        # Within the Rive
        i: int = 0
        while len(self.fish) > 0 and i < amount:
            self.fish.pop(0)
        i += 1
        return None
