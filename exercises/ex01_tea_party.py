"""Code for planning a Tea Party for 333 friends of mine & making it run smoothly"""

__author__: str = "730478204"


def main_planner(guests: int) -> None:
    """Function to call each function and produce printed output"""
    print("A Cozy Tea Party for " + str(guests) + " people!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: " + "$" + str(cost(tea_bags(guests), treats(guests))))
    return None


def tea_bags(people: int) -> int:
    """Computing # of tea bags needed for total # of guests"""
    return people * 2


def treats(people: int) -> int:
    """Computing # of treats needed for total # of guests"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Computing the cost of the sum of tea bags and treats for guests"""
    return float((tea_count * 0.50) + (treat_count * 0.75))


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
