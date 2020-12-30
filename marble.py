import sys
from collections import deque
sys.setrecursionlimit(10**9)
sys.stdin = open("input.txt", "r")
read = sys.stdin.readline

nodes, edges = list(map(int, read().rstrip().split()))
impossible = 0
edge = []
eachnode = set()
for _ in range(edges):
    lip = list(map(int, read().rstrip().split()))
    eachnode.add(lip[0])
    eachnode.add(lip[1])
    edge.append(lip)

# 스택에 중복된 값이 들어 갈 수 있으니, 중복방지 대책을 세워야한다
bigStk = []  # bigger than me
smallStk = []  # smaller than me


def big(num):
    global impossible, bigStk
    for node in edge:
        if node[1] == num and node not in bigStk:
            bigStk.append(node)
            if len(bigStk) >= nodes//2+1:
                impossible += 1
                break
            big(node[0])


def small(num):
    global impossible, smallStk
    for node in edge:
        if node[0] == num and node not in smallStk:
            smallStk.append(node)
            if len(smallStk) >= nodes//2+1:
                impossible += 1
                break
            small(node[1])


for i in eachnode:
    big(i)
    small(i)
    bigStk = []
    smallStk = []


print(impossible)
