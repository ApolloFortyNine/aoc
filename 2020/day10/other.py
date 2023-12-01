def count_arrangements(chargers):
    chargers.sort()  # Ensure the numbers are sorted
    n = len(chargers)
    dp = [0] * n  # dp[i] will store the number of valid arrangements ending with chargers[i]
    dp[0] = 1  # There's only one arrangement for the first element

    for i in range(1, n):
        for j in range(i-3, i):
            current = chargers[i]
            checking = chargers[j]
            if chargers[i] - chargers[j] <= 3:
                dp[i] += dp[j]
    print(dp)
    return dp[-1]  # The total count is the number of ways to reach the last number