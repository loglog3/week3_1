import sys
from collections import deque 


sys.stdin = open("input.txt", "r")

N, M = map(int,sys.stdin.readline().split())
maze = [list(map(int, list(str(sys.stdin.readline().rstrip())))) for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
check = deque([[0,0]])
maze[0][0] = 0
cnt = 1


while check:
    cnt += 1
    for i in range(len(check)):
        node = check.pop()
        x = node[0]
        y = node[1]

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
                check.appendleft([nx,ny])
                maze[nx][ny] = 0
                if nx == N-1 and ny == M-1:
                    print(cnt)
                    exit()