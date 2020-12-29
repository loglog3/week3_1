from collections import deque
import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10**6)
read = sys.stdin.readline

nodes = int(read())+1
edges = int(read())  # compare

queue = deque()
inDegree = [0 for _ in range(nodes)]
graph = [[] for _ in range(nodes)]
result = [0] * nodes
basic = [True for _ in range(nodes)]

# 차수, 그래프 완성
for _ in range(edges):
    main, sub, weight = list(map(int, read().rstrip().split()))
    graph[main].append((sub, weight))
    basic[main] = False
    inDegree[sub] += 1

# for i in graph:
#     print(i)
# for i in inDegree:
#     print(i)

# 첫 Q 넣기 - 임의로 설정
queue.append((nodes-1, 1))

# 빼면서 차수 조정
while queue:
    main, weight = queue.popleft()

    sublist = graph[main]
    for sub, sub_piece in sublist:
        inDegree[sub] -= 1
        result[sub] += weight * sub_piece
        if inDegree[sub] == 0:
            queue.append((sub, result[sub]))

# print(result)
# print(basic)
for i in range(1, nodes):
    if basic[i]:
        print(i, result[i])
