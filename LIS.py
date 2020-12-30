import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline
size = int(read())
A = list(map(int, read().rstrip().split()))

dp = [1] * (size)

for i in range(size):
    for j in range(i):
        if A[j] < A[i]:
            if dp[j]+1 > dp[i]:
                dp[i] = dp[j]+1

# print(dp)
print(max(dp))
