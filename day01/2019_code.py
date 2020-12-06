#get data
import os
scriptdir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(scriptdir,'2019_input.txt')) as data:
    modules = [int(x.strip()) for x in data.readlines()]

def FuelCounterUpper(module):
    return int(module / 3) - 2

def FuelCounterUpperHIGHIQ(module):
    fuelRequired = FuelCounterUpper(module)
    totalFuel = fuelRequired
    while FuelCounterUpper(fuelRequired) > 0:
        fuelRequired = FuelCounterUpper(fuelRequired)
        totalFuel += fuelRequired
    return totalFuel

assert FuelCounterUpper(12) == 2
assert FuelCounterUpper(14) == 2
assert FuelCounterUpper(1969) == 654
assert FuelCounterUpper(100756) == 33583
print(sum([FuelCounterUpper(x) for x in modules]))

assert FuelCounterUpperHIGHIQ(12) == 2
assert FuelCounterUpperHIGHIQ(14) == 2
assert FuelCounterUpperHIGHIQ(1969) == 966
assert FuelCounterUpperHIGHIQ(100756) == 50346
print(sum([FuelCounterUpperHIGHIQ(x) for x in modules]))