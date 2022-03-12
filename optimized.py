from typing import Sequence, Tuple
from openpyxl import load_workbook
from math import ceil

wb1 = load_workbook("dataset1_Python_P7.xlsx")
ws1 = wb1.active

weights_table1 = []
percentage_profits_table1 = []
for val in ws1.values:
    name, weight, percentage_profit = val[0].split(',')
    weights_table1.append(weight)
    percentage_profits_table1.append(percentage_profit)

# converting prices from string to float except for the first item ('price')
weights_table1 = [float(weight) for weight in weights_table1[1:]]

# converting profits from string to float except for the first item ('profit')
percentage_profits_table1 = [float(percentage)
                             for percentage
                             in percentage_profits_table1[1:]]


wb2 = load_workbook("dataset2_Python_P7.xlsx")
ws2 = wb2.active

weights_table2 = []
percentage_profits_table2 = []
for val in ws2.values:
    name, weight, percentage_profit = val[0].split(',')
    weights_table2.append(weight)
    percentage_profits_table2.append(percentage_profit)

# converting prices from string to float except for the first item ('price')
weights_table2 = [float(weight) for weight in weights_table2[1:]]

# converting profits from string to float except for the first item ('profit')
percentage_profits_table2 = [float(percentage)
                             for percentage
                             in percentage_profits_table2[1:]]


def what_profit(profits_percentage: Sequence,
                weights: Sequence) -> Sequence:
    """given the weights and the percentages taken, returns the profits done."""
    profits = []
    for cost, percentage in zip(weights, profits_percentage):
        profits.append(cost * (percentage / 100))
    return profits


def max_profit_dynamic(weights: Sequence[int],
                       profits_percentage: Sequence[int],
                       capacity: int) -> Tuple[list, int]:

    profits = what_profit(profits_percentage, weights)

    # in order to make the dynamic func work, we need make out of weights
    # a list of integers. We will use ceil to avoid exceed the limit.
    weights = [ceil(w) for w in weights]

    # cleaning corrupted data
    weights = [-w if w < 0 else w for w in weights]

    # the +1 in capacity and +1 in range is so that we can let
    # the first column == 0
    table = [[0 for _ in range(capacity + 1)] for _ in range(len(weights) + 1)]

    for i in range(len(weights)):  # remember weights and profits are \\ seqs.
        for c in range(1, capacity + 1):  # we want to keep the first col == 0.
            if weights[i] <= c:
                table[i + 1][c] = max(table[i][c],
                                      profits[i] + table[i][c - weights[i]])

    # in order to know which shares we selected.
    idx = len(weights)
    max_cap = capacity
    bag = []
    while idx > 0 and max_cap > 0:
        if table[idx - 1][max_cap] == table[idx][max_cap]:
            idx -= 1
        else:
            bag.append(weights[idx - 1])
            max_cap -= weights[idx - 1]
            idx -= 1

    return bag, table[-1][-1]
