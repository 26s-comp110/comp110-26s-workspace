"""EX07 - River Simulation"""

__author__ = "730926082"
from ex07.river import River

# contruct a river named my river with 10 fish and 2 bears
my_river: River = River(10, 2)


print(my_river)
# test out the functionality of one_river_week by calling it
my_river.one_river_week()
