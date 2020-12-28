import sys
from collections import deque
sys.stdin = open("input.txt", "r")
read = sys.stdin.readline

nodes, edges = list(map(int, read().rstrip().split()))
inDegree = [0] * (nodes+1)
queue = deque()
result = []
relation = [[0] for _ in range(nodes+1)]  # 하나의 frm에서 to가 여러게일수 있음

for i in range(edges):
    frm, to = list(map(int, read().rstrip().split()))
    inDegree[to] += 1
    relation[frm].append(to)

for i in range(1, len(inDegree)):
    if inDegree[i] == 0:
        queue.append(i)

while queue:
    i = queue.popleft()
    result.append(i)
    frm = relation[i]
    for j in frm:
        inDegree[j] -= 1
        if inDegree[j] == 0:
            queue.append(j)
print(*result, sep=' ')
