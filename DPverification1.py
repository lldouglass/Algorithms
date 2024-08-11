import time
def get_tree_segments_from_input():
    j = int(input().strip())
    segment_values = list(map(int, input().strip().split()))
    return segment_values


def T(i, j, segmentValueArray):
    if i > j:  # Base case for recursion
        return 0
    if i == j:
        return segmentValueArray[i]
    if j == i + 1:
        return max(segmentValueArray[i], segmentValueArray[j])
    return max(segmentValueArray[i] + min(T(i + 2, j, segmentValueArray), T(i + 1, j - 1, segmentValueArray)),
               segmentValueArray[j] + min(T(i + 1, j - 1, segmentValueArray), T(i, j - 2, segmentValueArray)))

# Get segment values from user input
segmentValueArray = get_tree_segments_from_input()
#t0 = time.time()
result = T(0, len(segmentValueArray) - 1, segmentValueArray)
#t1 = time.time()
secondInput = input()
numbersList = secondInput.split()
numbersList = [int(item) for item in numbersList]
#totalTime = t1-t0
print(result)
#print(time)




