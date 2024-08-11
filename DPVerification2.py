import time

def get_tree_segments_from_input():
    j = int(input().strip())
    segment_values = list(map(int, input().strip().split()))
    return segment_values

def T(i, j, segmentValueArray, memo):
    if i > j:
        return 0
    if i == j:
        return segmentValueArray[i]
    if j == i + 1:
        return max(segmentValueArray[i], segmentValueArray[j])
    
    if memo[i][j] != -1:
        return memo[i][j]
    
    memo[i][j] = max(segmentValueArray[i] + min(T(i + 2, j, segmentValueArray, memo), T(i + 1, j - 1, segmentValueArray, memo)),
                     segmentValueArray[j] + min(T(i + 1, j - 1, segmentValueArray, memo), T(i, j - 2, segmentValueArray, memo)))
    return memo[i][j]

# Get segment values from user input
segmentValueArray = get_tree_segments_from_input()
n = len(segmentValueArray)
memo = [[-1 for _ in range(n)] for _ in range(n)]

result = T(0, n - 1, segmentValueArray, memo)

print(result)
