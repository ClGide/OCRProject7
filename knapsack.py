from typing import Sequence, Tuple

test0 = {
    'input': {
        'capacity': 165,
        'weights': [23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
        'profits': [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
    },
    'output': 309
}

test1 = {
    'input': {
        'capacity': 3,
        'weights': [4, 5, 6],
        'profits': [1, 2, 3]
    },
    'output': 0
}

test2 = {
    'input': {
        'capacity': 4,
        'weights': [4, 5, 1],
        'profits': [1, 2, 3]
    },
    'output': 3
}

test3 = {
    'input': {
        'capacity': 170,
        'weights': [41, 50, 49, 59, 55, 57, 60],
        'profits': [442, 525, 511, 593, 546, 564, 617]
    },
    'output': 1735
}

test4 = {
    'input': {
        'capacity': 15,
        'weights': [4, 5, 6],
        'profits': [1, 2, 3]
    },
    'output': 6
}

test5 = {
    'input': {
        'capacity': 15,
        'weights': [4, 5, 1, 3, 2, 5],
        'profits': [2, 3, 1, 5, 4, 7]
    },
    'output': 19
}

tests = [test0, test1, test2, test3, test4, test5]

"""
The goal is to use memoization to optimize the working of this function. In other
words, each time the same combo is given as arg to the function, instead of 
calculating anew the result, we retrieve the result. 
Given that amongst the args, the only one to change are capacity and idx, I need to 
store the two. Then, whenever the same combo comes along, instead recomputing, I 
retrieve the result. 
"""

# the most we can spend on a client.
max_capacity = 500

# cost per share.
weights = [20, 30, 50, 70, 60, 80, 22, 26, 48, 34, 42, 110, 38,
          14, 18, 8, 4, 10, 24, 114]

# profit made by the share after 2 years.
# The profit is a percentage of the cost of the share.
profits_percentage = [5, 10, 15, 20, 17, 25, 7, 11, 13, 27, 17, 9, 23, 1,
          3, 8, 12, 14, 21, 18]

profits = []
for cost_percentage in zip(weights, profits_percentage):
    cost = cost_percentage[0]
    percentage = cost_percentage[1]
    profits.append(cost * (percentage / 100))


memo = {}


def max_profit_recursive(weights: Sequence[int],
                         profits: Sequence[int],
                         capacity: int, idx: int=0) -> int:

    if (capacity, idx) in memo.keys():
        return memo[capacity, idx]

    if idx == len(weights):
        memo[(capacity, idx)] = 0
        return memo[(capacity, idx)]
    elif weights[idx] > capacity:
        memo[(capacity, idx)] = max_profit_recursive(weights, profits, capacity, idx+1)
        return memo[(capacity, idx)]
    else:
        option1 = max_profit_recursive(weights, profits, capacity, idx+1)
        option2 = profits[idx] + max_profit_recursive(weights,
                                                      profits,
                                                      capacity-weights[idx],
                                                      idx+1)
        memo[(capacity, idx)] = max(option1, option2)
        return memo[(capacity, idx)]


def max_profit_dynamic(weights: Sequence[int],
                         profits: Sequence[int],
                         capacity: int) -> Tuple[list,int]:

    # the +1 in capacity and +1 in range is so that we can let
    # the first column == 0
    table = [[0 for _ in range(capacity+1)] for _ in range(len(weights)+1)]

    for i in range(len(weights)):   # remember weights and profits are \\ seqs.
        for c in range(1, capacity+1):    # we want to keep the first col == 0.
            if weights[i] <= c:
                table[i+1][c] = max(table[i][c],
                                    profits[i] + table[i][c-weights[i]])

    # in order to know which shares we selected.
    idx = len(weights)
    max_cap = capacity
    bag = []
    while idx > 0 and max_cap > 0:
        if table[idx-1][max_cap] == table[idx][max_cap]:
            idx -= 1
        else:
            bag.append(weights[idx-1])
            max_cap -= weights[idx-1]
            idx -=1

    return bag, table[-1][-1]


# be aware that you are recreating new tables for each outer loop.
# You might try
# to avoid that.
# Another inefficiency is that after computing
# the given row, all the below rows
# are also filled.

res = max_profit_dynamic(weights, profits, max_capacity)
