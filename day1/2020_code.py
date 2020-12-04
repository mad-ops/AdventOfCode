#get data
import os
scriptdir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(scriptdir,'2020_input.txt')) as expenses:
    expenseList = [int(x.strip()) for x in expenses.readlines()]

#part one
## very simple, create a cache of numbers we're
## searching for and return when we find one
def pairwise_haystack(expenses):
    cache = []
    for expense in expenses:
        cache.append(expense)
        partner = 2020 - expense
        if partner in cache:
            return partner * expense

#part two
import itertools
from math import prod
def trip_haystack(expenses):
    # Lets create a dict key'd by sum of pairs
    pairwise_expenses = {}
    for pair in list(itertools.combinations(expenses, 2)):
        if sum(pair) > 2020:
            continue

        pairwise_expenses[sum(pair)] = pair

    # Loop through expenses to see if we have
    # the matching pairwise sum, then return
    for expense in expenses:
        if 2020 - expense in pairwise_expenses:
            return expense * prod(pairwise_expenses[2020-expense])

if __name__ == "__main__":
    print(pairwise_haystack(expenseList))
    print(trip_haystack(expenseList))