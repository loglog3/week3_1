import sys
from collections import deque

sys.stdin = open("input.txt", "r")

N, M = map(int,sys.stdin.readline().split())
matrix = [[] for _ in range(N+1)]

# 데이터를 받아서 matrix[start]에 경로를 저장함
for m in range(M):
    start, end = map(int,sys.stdin.readline().split())
    matrix[start].append(end)

# print(matrix)

check = deque([])
visited = [False]*(N+1)

def DFS(node):
    # print("node:", node)
    while matrix[node]:
        # print("matrix[node]:", matrix[node])
        cur = matrix[node].pop()
        if visited[cur] != True:
            DFS(cur)
    check.appendleft(node)
    visited[node] = True
    # print("visited:", visited)
     

for i in range(1,N+1):
    # print("i:", i)
    if visited[i] != True:
        DFS(i)

print(*check)