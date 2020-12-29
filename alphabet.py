import sys
from collections import deque
# sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "r")
read = sys.stdin.readline

h, w = list(map(int, read().rstrip().split()))

board = [list(read().rstrip()) for _ in range(h)]

maxStage = 0
# stack으로 풀기
# DFS stack 사용 시, 경로를 stack에 함께 넣어줘버린다음에.
# pop 으로 뺴내는 스킬을 쓰면 좋다!
stack = deque()
stack.append([0, 0, board[0][0]])
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

# DFS
maxPath = ''
while stack:
    r, c, path = stack.pop()
    maxPath = path if len(maxPath) < len(path) else maxPath
    for t in range(4):
        nr = r + dr[t]
        nc = c + dc[t]
        # letter = board[nr][nc]
        if -1 < nr < h and -1 < nc < w and board[nr][nc] not in path:
            stack.append([nr, nc, path + board[nr][nc]])
            # print(path)

print(len(maxPath))
# print(maxPath)

# 재귀로 풀기

# # 시간초과


# def pathDFS(row, col, stage, visit):
#     global maxStage
#     maxStage = max(stage, maxStage)
#     if -1 < row-1 and map[row-1][col] not in visit:
#         pathDFS(row-1, col, stage+1, visit+map[row-1][col])
#     if row+1 < h and map[row+1][col] not in visit:
#         pathDFS(row+1, col, stage+1, visit+map[row+1][col])
#     if -1 < col-1 and map[row][col-1] not in visit:
#         pathDFS(row, col-1, stage+1, visit+map[row][col-1])
#     if col+1 < w and map[row][col+1] not in visit:
#         pathDFS(row, col+1, stage+1, visit+map[row][col+1])


# pathDFS(0, 0, 1, map[0][0])

# # # 또 시간초과
# visit = [map[0][0]] * 26  # 크기 미리 지정


# def pathDFS(row, col, stage):
#     global maxStage
#     maxStage = max(stage, maxStage)
#     if -1 < row-1 and map[row-1][col] not in visit:
#         visit.append(map[row-1][col])
#         pathDFS(row-1, col, stage+1)
#         visit.remove(map[row-1][col])
#     if row+1 < h and map[row+1][col] not in visit:
#         visit.append(map[row+1][col])
#         pathDFS(row+1, col, stage+1)
#         visit.remove(map[row+1][col])
#     if -1 < col-1 and map[row][col-1] not in visit:
#         visit.append(map[row][col-1])
#         pathDFS(row, col-1, stage+1)
#         visit.remove(map[row][col-1])
#     if col+1 < w and map[row][col+1] not in visit:
#         visit.append(map[row][col+1])
#         pathDFS(row, col+1, stage+1)
#         visit.remove(map[row][col+1])
# pathDFS(0, 0, 1)
# print(maxStage)
