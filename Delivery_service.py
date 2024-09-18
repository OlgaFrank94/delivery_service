"""Номер удачного теста 118239780."""
from typing import List


def min_platforms(robot_weights: List[int], limit: int) -> int:
    """
    Определяет минимальное количество транспортных платформ.

    Которые необходимы для перевозки всех роботов.

    Args:
        robot_weights (List[int]): Список весов роботов.
        limit (int): Предельная грузоподъёмность платформы.

    Returns:
        int: Минимальное количество необходимых платформ.
    """
    platforms = 0
    robots = sorted(robot_weights)

    while robots:
        if len(robots) == 1 or robots[-1] + robots[0] > limit:
            robots.pop()
            platforms += 1
        else:
            robots.pop(0)
            robots.pop()
            platforms += 1

    return platforms


if __name__ == "__main__":
    robot_weights = [int(x) for x in input().split()]
    platform_limit = int(input())
    print(min_platforms(robot_weights, platform_limit))
