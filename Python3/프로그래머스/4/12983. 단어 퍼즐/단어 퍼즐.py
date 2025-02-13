def solution(strs, t):
    word_set = set(strs)
    dp = [float('inf')] * (len(t) + 1)
    dp[0] = 0

    for i in range(len(t)):
        if dp[i] == float('inf'):
            continue

        for length in range(1, 6):
            if i + length <= len(t) and t[i:i+length] in word_set:
                dp[i + length] = min(dp[i + length], dp[i] + 1)

    return dp[len(t)] if dp[len(t)] != float('inf') else -1