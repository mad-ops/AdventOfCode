#get data
import os
scriptdir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(scriptdir,'2020_input.txt')) as expenses:
    expenseList = [int(x.strip()) for x in expenses.readlines()]

#part one
def pairwise_haystack(expenses):
    cache = []
    for expense in expenses:
        cache.append(expense)
        partner = 2020 - expense
        if partner in cache:
            return partner * expense

#part two
import itertools
def trip_haystack(expenses):
    return [sum(i) for i in list(itertools.combinations(expenses, 2))]

if __name__ == "__main__":
    print(pairwise_haystack(expenseList))
    print(trip_haystack(expenseList))