import sys
sys.setrecursionlimit(10**9)
sys.stdin = open("input.txt", "r")

read = sys.stdin.readline
n = int(read())

basic = [[] for i in range(n+1)]
parents = [0 for i in range(n+1)]

for i in range(n-1):
    a, b = map(int, read().split())
    basic[a].append(b)
    basic[b].append(a)
print('basic', basic)


def DFS(i, basic, parent):
    if parents[i] == 0:
        parents[i] = parent
        for j in basic[i]:
            DFS(j, basic, i)
    return
# 부모에서 자식들을 타고 들어가는 형태다.
# 나랑 연결된 애들은 다 내 자식이다.


DFS(1, basic, 1)
print(parents)
