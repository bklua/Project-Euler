# Coin sums
# Problem 31

def coin_sum(coins, amounts):
    dp = [0] * (amounts + 1)
    dp[0] = 1
    
    for coin in coins:
        for amount in range(1, amounts + 1):
            if amount >= coin: dp[amount] += dp[amount - coin]
    return dp[-1]

print(coin_sum([1,2,5,10,20,50,100,200], 200))