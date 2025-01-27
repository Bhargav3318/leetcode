def candy(ratings):
    n = len(ratings)
    dp = [1]*n
    #left to right
    for i in range(1,n):
        if ratings[i]>ratings[i-1] and dp[i]<=dp[i-1]:
            dp[i] = dp[i-1]+1
        #right to left
    for i in range(n-2,-1,-1):
        if ratings[i]>ratings[i+1] and dp[i]<=dp[i+1]:
            dp[i] = dp[i+1]+1
    return sum(dp)

print(candy(list(map(int, input().split()))))