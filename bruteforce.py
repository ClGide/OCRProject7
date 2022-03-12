from itertools import combinations
from typing import Sequence, Generator, Tuple

# the most we can spend on a client.
max_capacity = 500

# cost per share.
weights = [20, 30, 50, 70, 60, 80, 22, 26, 48, 34, 42, 110, 38,
           14, 18, 8, 4, 10, 24, 114]

# profit made by the share after 2 years.
# The profit is a percentage of the cost of the share.
profits_percentage = [5, 10, 15, 20, 17, 25, 7, 11, 13, 27, 17, 9, 23, 1,
                      3, 8, 12, 14, 21, 18]


"""
What we need to do is to go through all possible combinations. Check that their 
weight isn't above capacity. Return the most valuable combination. 
"""


def all_combinations(items: Sequence[Tuple[int, int]]) -> Generator:
    """Generates all possible combinations of items"""
    return (comb
            for r in range(1, len(items)+1)
            for comb in combinations(items, r)
            )


def total_value(combination: Sequence[Tuple[int, int]],
                capacity: int) -> Tuple[Sequence[Tuple[int, int]], int, int]:
    """Generates the value of a combination of items"""
    total_weight = total_value = 0
    for weight, value in combination:
        total_weight += weight
        total_value += value
    return (combination, total_value, total_weight) if total_weight <= capacity else (0, 0)


def what_profit(profits_percentage: Sequence,
                weights: Sequence) -> Sequence:
    """given the weights and the percentages taken, returns the profits done."""
    profits = []
    for cost, percentage in zip(weights, profits_percentage):
        profits.append(cost * (percentage / 100))
    return profits


def bag(weights: Sequence, profits_percentage: Sequence,
        capacity: int) -> Tuple[Sequence[Tuple[int, int]], int, int]:
    """solves the 0/1 KP by returning the chosen items, their total value
    and their total weight. """
    profits = what_profit(profits_percentage, weights)
    items = list(zip(weights, profits))

    values_weights = [total_value(combination, capacity) for combination in all_combinations(items)]
    bagged = max(values_weights, key=lambda x: x[1:])
    return bagged


res = bag(weights, profits_percentage, max_capacity)
