import time 
import sys
sys.setrecursionlimit(5000)

def treeSegment():
    j = int(input().strip())
    segment_values = list(map(int, input().strip().split()))
    return segment_values

# Bottom-up with traceback
def TbottomUp(segmentValueArray):
    n = len(segmentValueArray)
    # Initialize the DP table with tuples (0, None)
    dp = [[(0, None) for _ in range(n)] for _ in range(n)]

    # Fill the DP table
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            # Base case
            if i == j:
                dp[i][j] = (segmentValueArray[i], 'L')
                continue
            chooseLeft = segmentValueArray[i] + min(dp[i + 2][j][0] if i + 2 <= j else 0,
                                                    dp[i + 1][j - 1][0] if i + 1 <= j - 1 else 0)
            chooseRight = segmentValueArray[j] + min(dp[i + 1][j - 1][0] if i + 1 <= j - 1 else 0,
                                                     dp[i][j - 2][0] if i <= j - 2 else 0)
            if chooseLeft >= chooseRight:
                dp[i][j] = (chooseLeft, 'L')
            else:
                dp[i][j] = (chooseRight, 'R')

    return dp


#find the sequence of picks
def traceback(dp, n):
    sequence = []
    i, j = 0, n - 1
    turn = True  # True for your turn and False for neighbor turn

    for _ in range(2 * n):  # Upper bound on the number of iterations
        if i > j:
            break 
        if turn:
            choice = dp[i][j][1]
            sequence.append(i + 1 if choice == 'L' else j + 1)
            if choice == 'L':
                i += 1
            else:
                j -= 1

        turn = not turn

    return sequence


#execution
segmentValueArray = treeSegment()
dp_table = TbottomUp(segmentValueArray)
result, _ = dp_table[0][len(segmentValueArray)-1]
sequence = traceback(dp_table, len(segmentValueArray))
print(result)
print(' '.join(map(str, sequence)))
