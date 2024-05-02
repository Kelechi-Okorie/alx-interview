#!/usr/bin/python3
"""Making change"""


def makeChange(coins, total):
    # If total is 0 or less, return 0
    if total <= 0:
        return 0

    # Sort the coins in descending order
    coins.sort(reverse=True)

    # Initialize a variable to store the number of coins needed
    num_coins = 0

    # Iterate through each coin value
    for coin in coins:
        # Calculate how many coins of the current denomination can be used
        num_of_coins = total // coin
        # Update the total amount
        total -= num_of_coins * coin
        # Update the number of coins needed
        num_coins += num_of_coins

        # If total becomes 0, break the loop
        if total == 0:
            break

    # If total is still greater than 0, total cannot be met by
    # any number of coins
    if total > 0:
        return -1

    # Return the number of coins needed
    return num_coins
