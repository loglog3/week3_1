import sys
import copy
from collections import deque 

sys.stdin = open("input.txt","r")

N, M = map(int,sys.stdin.readline().split())

iceberg = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

meltdown = deque([])

dx = [0,-1,0,1]
dy = [-1,0,1,0]

# 초기 좌표
for n in range(N):
    for m in range(M):
        if iceberg[n][m] != 0:
            meltdown.append([n,m])
# print("year:",0,"meltdown:",meltdown)

year = 1

# 시작
while meltdown:
    # 1. 빙하-해수면 탐색
    for i in range(len(meltdown)):
        temp = meltdown.popleft()
        x = temp[0]
        y = temp[1]
        melt_cnt = 0 
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            # 바다 탐색
            if 0 <= nx < N and 0 <= ny < M and iceberg[nx][ny] == 0:
                melt_cnt += 1

        # deque에 저장
        meltdown.append([x,y,melt_cnt])
    # print("melt_cnt:", meltdown)
            
            
    # 2. pop하면서 감소
    for i in range(len(meltdown)):
        temp = meltdown.popleft()
        iceberg[temp[0]][temp[1]] -= temp[2]
        if iceberg[temp[0]][temp[1]] <= 0:
            iceberg[temp[0]][temp[1]] = 0
        else:
            meltdown.append([temp[0],temp[1]])

    # print(meltdown)
    if not meltdown:
        print(0)
        exit()

    # 3. 빙하길이 탐색
    # 한 점에서 시작
    ex_cnt = 0
    explorer = copy.deepcopy(iceberg)
    check = deque([[meltdown[0][0],meltdown[0][1]]])
    # print("check:", check, "meltdown:", meltdown)
    while check:
        temp = check.popleft()
        x = temp[0]
        y = temp[1]
        # print("temp:", temp)

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M and explorer[nx][ny] > 0:
                explorer[nx][ny] = 0
                ex_cnt += 1
                check.append([nx,ny])
    # print("ex_cnt:", ex_cnt, "len(meltdown):", len(meltdown))
    if ex_cnt != len(meltdown):
        print(year)
        exit()

    check.clear()
    explorer.clear()

    # print("iceberg:", iceberg)


    # print("year:", year, "meltdown:", meltdown)
    year += 1