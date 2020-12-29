import sys
sys.setrecursionlimit(10**7)
sys.stdin = open("input.txt", "r")
read = sys.stdin.readline


def ripen():
    # days = 0
    queue = []

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if arr[i][j][k] == 1:
                    queue.append([i, j, k])

    days = bfs(queue)

    # 익지 못한 과일이 있는지 확인
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if arr[i][j][k] == 0:
                    return -1
    return days


def bfs(queue):
    days = -1
    tmp = []

    while len(queue) != 0:
        for pos in queue:
            x = pos[0]
            y = pos[1]
            z = pos[2]

            for t in range(6):  # 6방향으로 움직임
                nx = x + dx[t]
                ny = y + dy[t]
                nz = z + dz[t]
                if -1 < nx < h and -1 < ny < n and -1 < nz < m and arr[nx][ny][nz] == 0:
                    arr[nx][ny][nz] = 1
                    tmp.append([nx, ny, nz])
        days += 1
        queue = tmp
        tmp = []

    return days


dx = [-1, 1, 0, 0, 0, 0]  # 위아래
dy = [0, 0, -1, 1, 0, 0]  # 뒤앞
dz = [0, 0, 0, 0, -1, 1]  # 좌우

input = sys.stdin.readline
m, n, h = map(int, read().rstrip().split())
# 이렇게 배열을 만들 수 있다
arr = [[list(map(int, read().rstrip().split()))
        for _ in range(n)] for _ in range(h)]
answer = 0

print(ripen())
