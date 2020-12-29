import sys
sys.stdin = open("input.txt", "r")

N, M = map(int,sys.stdin.readline().split())

visited_forward = [0]*(N+1)
visited_reverse = [0]*(N+1)
matrix_forward = [[] for row in range(N+1)]
matrix_reverse = [[] for row in range(N+1)]
# visited[0] = 순방향, visited[1] = 역방향

for m in range(M):
    start, end = map(int,sys.stdin.readline().split())
    matrix_forward[start].append(end)
    matrix_reverse[end].append(start)

def DFS_forward(start, N):
    global cnt
    cnt += 1
    visited_forward[start]=1
    if cnt > N//2:
        return 

    if not matrix_forward:
        return 

    else:
        for i in matrix_forward[start]:
            if visited_forward[i] == 0:
                DFS_forward(i,N)
        return

def DFS_reverse(start, N):
    global cnt
    cnt += 1
    visited_reverse[start]=1
    if cnt > N//2:
        return 

    if not matrix_reverse:
        return 

    else:
        for i in matrix_reverse[start]:
            if visited_reverse[i] == 0:
                DFS_reverse(i,N)
        return

result = 0

for i in range(1,N+1):
    visited_forward = [0]*(N+1)
    cnt = -1
    if visited_forward[i] == 0:
        DFS_forward(i,N)
        if cnt > N//2:
            result += 1

    visited_reverse = [0]*(N+1)
    cnt = -1
    if visited_reverse[i] == 0:
        DFS_reverse(i,N)
        if cnt > N//2:
            result += 1




print(result)