import sys

sys.setrecursionlimit(10**6)

sys.stdin = open("input.txt", "r")

read = sys.stdin.readline
nodeNum, edgeNum, start = list(map(int, read().split()))
edges = []
for i in range(edgeNum):
    edges.append(list(map(int, input().split())))

mat = []
for _ in range(nodeNum):
    mat.append([0]*nodeNum)

for _ in range(nodeNum):
    print(mat[_])


print()
print(edges)
print()
for idx in range(len(edges)):
    mat[edges[idx][0]-1][edges[idx][1]-1] = 1
    mat[edges[idx][1]-1][edges[idx][0]-1] = 1

for _ in range(nodeNum):
    print(mat[_])


def dfs(start):
    dfsStk.append(start)
    for row in range(nodeNum):
        mat[row][start-1] = 0
    for i in range(nodeNum):
        if mat[start-1][i] == 1:
            dfs(i+1)


dfsStk = []
dfs(start)
# print('dfs', dfsStk)
print(*dfsStk, sep=' ')


# 행렬 다시만들기
for idx in range(len(edges)):
    mat[edges[idx][0]-1][edges[idx][1]-1] = 1
    mat[edges[idx][1]-1][edges[idx][0]-1] = 1


def bfs(start):
    if not bfsStk:
        bfsStk.append(start)
    for row in range(nodeNum):
        mat[row][start-1] = 0

    for i in range(nodeNum):
        if mat[start-1][i] == 1:
            bfsStk.append(i+1)
            children.append(i+1)
            for row in range(nodeNum):
                mat[row][i] = 0
            if len(bfsStk) == nodeNum:
                return
    for _ in children:
        child = children.pop(0)
        bfs(child)


bfsStk = []
children = []
bfs(start)
# print('bfs', bfsStk)
print(*bfsStk, sep=' ')
