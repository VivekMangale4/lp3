def knapsack_01(capacity, weights, values, n):
    dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0  
            elif weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]

n = int(input("Enter number of items : "))
weights = []
values = []
for i in range(n):
    values.append(int(input("Enter value of items : ")))
    weights.append(int(input("Enter weight of items : ")))
capacity = int(input("Enter capacity of bag : "))
max_value = knapsack_01(capacity, weights, values, n)
print(f"Maximum value in knapsack = {max_value}")
