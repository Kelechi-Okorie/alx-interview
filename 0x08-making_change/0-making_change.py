#!/usr/bin/python3
"""Making change"""


def makeChange(coins, total):
    # If total is 0 or less, return 0
    if total <= 0:
        return 0

    # Initialize an array to store the fewest number of coins needed
    # for each amount from 0 to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins needed to make amount 0

    # Iterate through each coin value
    for coin in coins:
        # Update dp array for each amount from coin value to total
        for amount in range(coin, total + 1):
            # Update dp[amount] with the minimum of current value
            # and dp[amount - coin] + 1
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If the value of dp[total] is still infinity, total cannot be
    # met by any number of coins
    if dp[total] == float('inf'):
        return -1

    # Return the fewest number of coins needed for total
    return dp[total]
