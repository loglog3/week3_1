import sys
from collections import deque


sys.stdin = open("input.txt", "r")
# sys.stdout = open('output.txt','w')
# sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
need_parts = [[] for row in range(N+1)]
parts_needed = [0]*(N+1)
EA_list = [0]*(N+1)
visited = [0]*(N+1)
basic = []

for m in range(M):
    x, y, EA = map(int,sys.stdin.readline().split())
    need_parts[x].append([y,EA])
    parts_needed[y] += 1

# print("need_parts:",need_parts)
while sum(parts_needed) > 0:
    # 현 트리에서 제일 위에 있는 친구를 찾음
    for i in range(1,N+1):
        if not need_parts[i] and visited[i] == 0:
            basic.append(i)
            visited[i] = 1
        if parts_needed[i] == 0 and visited[i] == 0:
            if EA_list[i] == 0:
                EA_list[i] = 1
            visited[i] = 1
            # print("i:", i)
            # need_parts에서 해당 idx를 찾는다.
            for j in need_parts[i]:
                EA_list[j[0]] += j[1]*EA_list[i]
                parts_needed[j[0]] -= 1

print("parts_needed:", parts_needed)
print("EA_list:", EA_list)
for i in basic:
    print(i, EA_list[i], sep=" ")



