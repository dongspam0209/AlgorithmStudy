import sys
input = sys.stdin.readline

n =int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)

s = 0
for i, j in zip(a, b):
    s += i*j

print(s)