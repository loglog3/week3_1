import sys
from collections import deque
# sys.setrecursionlimit(10**9)
sys.stdin = open("input.txt", "r")
read = sys.stdin.readline

h, w = list(map(int, read().rstrip().split()))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

map1 = [list(map(int, read().strip().split())) for _ in range(h)]
year = 0

queue = deque()


while True:
    big = 0
    small = 0
    # 넓이
    for r in range(1, h-1):
        for c in range(1, w-1):
            if map1[r][c] != 0:
                big += 1

    # 작은 넓이
    visited = []

    for r in range(1, h-1):
        for c in range(1, w-1):
            if map1[r][c] != 0:
                queue.append([r, c])
                break

    # 간단하게 queue로 만든 DFS
    while queue:
        r, c = queue.popleft()
        for t in range(4):
            nr = r + dx[t]
            nc = c + dy[t]
            if map1[nr][nc] != 0 and [nr, nc] not in visited:
                visited.append([nr, nc])
                small += 1
                queue.append([nr, nc])
    # 넓이 비교
    if small != big:
        print(year)
        break
    elif big == 0:
        print(0)
        break

    # 녹이기
    melted = []
    for r in range(1, h-1):
        for c in range(1, w-1):
            if map1[r][c] != 0:
                ice = map1[r][c]
                # 사방확인
                for t in range(4):
                    nr = r + dx[t]
                    nc = c + dy[t]
                    if map1[nr][nc] == 0:
                        ice -= 1
                        if ice == 0:
                            break
                melted.append([r, c, ice])
    for i in melted:
        map1[i[0]][i[1]] = i[2]

    year += 1
