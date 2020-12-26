from collections import deque
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open("input.txt", "r")
read = sys.stdin.readline

row_size, col_size = list(map(int, read().rstrip().split()))

maze = []
for row in range(row_size):
    maze.append(list(read().rstrip()))

# for i in maze:
#     print(i)

bfsQ = deque()


count = 0


def bfs(row, col, stage):
    global count
    # 지나온 곳은 다시 방문하지 않는다
    if maze[row][col] == '0':  # 다른 경로로 이미 방문했을 경우 return
        return
    maze[row][col] = '0'  # 방문 flag
    if row == row_size-1 and col == col_size-1:
        count = stage
        return
    # 상우하좌
    if row-1 >= 0 and maze[row-1][col] == '1':
        bfsQ.append([row-1, col, stage])
    if col+1 <= col_size-1 and maze[row][col+1] == '1':
        bfsQ.append([row, col+1, stage])
    if row+1 <= row_size-1 and maze[row+1][col] == '1':
        bfsQ.append([row+1, col, stage])
    if col-1 >= 0 and maze[row][col-1] == '1':
        bfsQ.append([row, col-1, stage])

    for _ in range(len(bfsQ)):
        if bfsQ:
            nextRow, nextCol, stage = bfsQ.popleft()
            bfs(nextRow, nextCol, stage + 1)


bfs(0, 0, 1)
# print('단계', count)
print(count)
