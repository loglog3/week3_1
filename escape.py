# * 물 -> 확산됨
# X 돌 -> 이동불가
# . 비어있음
# D 목적지
# S 고슴도치

import sys
sys.stdin = open("input.txt", "r")
read = sys.stdin.readline

h, w = list(map(int, read().rstrip().split()))

map = [list(read().rstrip()) for _ in range(h)]


waterQ = []
dochiQ = []


def water():
    # 현재 시각
    time = 0
    # 물 추가
    for r in range(h):
        for c in range(w):
            if map[r][c] == '*':
                waterQ.append([r, c])

    # 고슴도치 위치
    for r in range(h):
        for c in range(w):
            if map[r][c] == 'S':
                dochiQ.append([r, c])
    # 경주 시작 (물과 고슴도치를 넘겨줌)
    time = diffusion(waterQ, dochiQ)

    # 제대로 도착했는지 확인
    # for r in range(h):
    #     for c in range(w):
    #         if map[r][c] == 'D':
    #             return 'KAKTUS'
    return time


def diffusion(waterQ, dochiQ):
    time = 0
    waterTmp = []
    dochiTmp = []

    while waterQ or dochiQ:
        # waterQ 큐가 한번 비면, 시간이 한번 흐른 것
        for water in waterQ:
            r = water[0]
            c = water[1]
            for i in range(4):  # 좌우상하
                nr = r + dy[i]
                nc = c + dx[i]
                # 범위안에있고, 돌이 아니고 목적지가 아니고 이미 물이 아니면
                if -1 < nr < h and -1 < nc < w and map[nr][nc] != 'X' and map[nr][nc] != 'D' and map[nr][nc] != '*':
                    map[nr][nc] = '*'
                    waterTmp.append([nr, nc])

        # 물이 먼저 이동 후, 고슴도치가 이동
        for dochi in dochiQ:
            r = dochi[0]
            c = dochi[1]
            for i in range(4):  # 좌우상하
                nr = r + dy[i]
                nc = c + dx[i]
                # 범위안에있고, 돌이 아니고 물이 아니면
                if -1 < nr < h and -1 < nc < w and map[nr][nc] != 'X' and map[nr][nc] != '*' and map[nr][nc] != 'S':
                    if map[nr][nc] == 'D':
                        map[nr][nc] = 'S'
                        time += 1
                        return time
                    else:  # map[nr][nc] != 'D'
                        map[nr][nc] = 'S'
                    dochiTmp.append([nr, nc])

        waterQ = waterTmp
        dochiQ = dochiTmp
        # 더 이상 갈곳이 없으면, 죽음
        if not dochiQ:
            return 'KAKTUS'
        waterTmp = []
        dochiTmp = []

        # queue가 한번 돌고 나면, 시간 +=1
        time += 1
    return time


# move
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(water())
