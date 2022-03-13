from math import ceil
from typing import Sequence, Tuple, Dict

from openpyxl import load_workbook


def name_weights_profits(filename: str) -> Tuple[Sequence[int]]:
    """parses the excel worksheet and returns each share's price and
    bought percentage."""
    wb = load_workbook(filename)
    ws = wb.active

    names_table = []
    weights_table = []
    percentage_profits_table = []

    for val in ws.values:
        # the values are originally given in the worksheet in a csv style.
        name, weight, percentage_profit = val[0].split(',')
        names_table.append(name)
        weights_table.append(weight)
        percentage_profits_table.append(percentage_profit)

    # mapping the weights to their share
    weight_name = dict(zip(weights_table, names_table))
    weight_name.pop('price')
    weight_name = {ceil(float(key)): value for key, value in weight_name.items()}

    # converting prices from str to float except for the first item ('price')
    weights_table = [float(weight) for weight in weights_table[1:]]

    # in order to make the dynamic func below work, we need to return
    # a list of integers. We will use ceil to avoid exceeding the limit.
    weights_table = [ceil(w) for w in weights_table]

    # cleaning corrupted data
    weights_table = [-w if w < 0 else w for w in weights_table]

    # converting profits from str to float except for the first item ('profit')
    percentage_profits_table = [float(percentage)
                                for percentage
                                in percentage_profits_table[1:]]

    return weight_name, weights_table, percentage_profits_table


def what_profit(profits_percentage: Sequence,
                weights: Sequence) -> Sequence[float]:
    """given the weights and the percentages taken,
     returns the profits done."""
    profits = []
    for cost, percentage in zip(weights, profits_percentage):
        profits.append(cost * (percentage / 100))
    return profits


def max_profit_dynamic(weights: Sequence[int],
                       profits_percentage: Sequence[int],
                       capacity: int) -> Tuple[Sequence[int], int]:
    profits = what_profit(profits_percentage, weights)

    # the +1 in capacity and range is so that we can let
    # the first column == 0
    table = [[0 for _ in range(capacity + 1)] for _ in range(len(weights) + 1)]

    for i in range(len(weights)):
        for c in range(1,
                       capacity + 1):  # starts at 1 to keep the 1st col == 0.
            if weights[i] <= c:
                table[i + 1][c] = max(table[i][c],
                                      profits[i] + table[i][c - weights[i]])

    # parse the table to identify the chosen shares.
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


def parsing_data_return_shares(filename: str, capacity: int):
    """parses the excel file and returns the most profitable combination
     of shares that respects the max capacity constraint AND their total
      value. """

    weight_name, weights, profit_percentages = name_weights_profits(filename)
    bag, max_profit = max_profit_dynamic(weights, profit_percentages, capacity)
    bag = [weight_name[weight] for weight in bag]
    return bag, max_profit


if __name__ == "__main__":
    parsing_data_return_shares("dataset1_Python_P7.xlsx", 500)
   
