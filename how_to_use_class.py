import sys

sys.setrecursionlimit(10**6)

# sys.stdin = open("input.txt", "r")

read = sys.stdin.readline
nodeNum, edgeNum, start = list(map(int, read().split()))
edges = []
for i in range(edgeNum):
    edges.append(list(map(int, input().split())))


class Node:
    def __init__(self, me):
        self.me = me
        self.parent = None
        self.children = []

    def append(self, child):
        self.children.append(child)


nodes = []
for edge in edges:
    if edge[0] > edge[1]:
        edge[0], edge[1] = edge[1], edge[0]
    if edge[1] == start:
        edge[0], edge[1] = edge[1], edge[0]

    print(edge)
    globals()['node'+str(edge[0])] = Node(edge[0])

for i in range(1, 4):
    print(eval('node'+str(i)).me)
