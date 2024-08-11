import time

def treeSegment():
    j = int(input().strip())
    segment_values = list(map(int, input().strip().split()))
    return segment_values

# Bottom-up
def TbottomUp(segmentValueArray):
    n = len(segmentValueArray)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    # Base cases
    for i in range(n):
        dp[i][i] = segmentValueArray[i]
    # DP table
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if j == i + 1:
                dp[i][j] = max(segmentValueArray[i], segmentValueArray[j])
            else:
                dp[i][j] = max(segmentValueArray[i] + min(dp[i + 2][j], dp[i + 1][j - 1]),
                               segmentValueArray[j] + min(dp[i + 1][j - 1], dp[i][j - 2]))

    return dp[0][n-1]
segmentValueArray = treeSegment()
result = TbottomUp(segmentValueArray)
print(result)