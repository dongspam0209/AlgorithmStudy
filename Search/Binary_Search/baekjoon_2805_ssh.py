import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
start, end = 0, max(trees)

while start <= end:
    mid = (start + end) // 2
    length = 0
    for tree in trees:
        if tree > mid:
            length += (tree - mid)
    
    if length >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)