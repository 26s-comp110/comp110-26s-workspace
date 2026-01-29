def can_eat(allergic: bool) -> bool:
    """Is it safe to eat this food?"""
    return not allergic


print(can_eat(allergic=True))
