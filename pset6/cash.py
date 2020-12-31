# Imports libraries.
import cs50
import time

# Initializes constants.
QUARTERS = .25
DIMES = .10
NICKELS = .05
PENNIES = .01

# Gets Input.
change = cs50.get_float("Change owed: ")

# Tests, and if needed, rerequests input.
while change < 0:
    change = cs50.get_float("Change Owed: ")

# Intializes counter.
counter = 0

# Counts quarters.
while change >= QUARTERS:
    change = change - QUARTERS
    counter += 1

# Rounds change to clear junk values.
change = round(change, 2)

# Counts dimes.
while change >= DIMES:
    change = change - DIMES
    counter += 1

# Rounds change to clear junk values.
change = round(change, 2)

# Counts nickels.
while change >= NICKELS:
    change = change - NICKELS
    counter += 1

# Rounds change to clear junk values.
change = round(change, 2)

# Counts pennies.
while change >= PENNIES:
    change = change - PENNIES
    counter += 1

# Returns total coin amount.
print(counter)
