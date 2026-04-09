"""File to define Fish class."""


class Fish:

    age: int

    def __init__(self):
        """docstring"""
        self.age = 0
        return None

    def one_day(self):
        """docstring"""
        # It should increase the value of the age attribute by one
        self.age += 1
        return None
