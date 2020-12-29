import sys
from collections import deque

sys.stdin = open("input.txt","r")

rotten = deque()
zero = 0
one = 0
Y, X, H = map(int,sys.stdin.readline().split())
tomato = [[] for _ in range(H)]
for h in range(H):
    for j in range(X):
        temp = list(map(int,sys.stdin.readline().split()))
        tomato[h].append(temp)
        for k in range(len(temp)):
            if temp[k] == 0:
                zero += 1
            elif temp[k] == 1:
                one += 1
                rotten.appendleft([h, j, k])

day = 0
dx = [0, -1, 0, 1, 0, 0]
dy = [-1, 0, 1, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def rotting(X,Y,H, day):
    global zero
    while rotten:
        day += 1

        for i in range(len(rotten)):
            temp = rotten.pop()
            z = temp[0]
            x = temp[1]
            y = temp[2]

            for d in range(6):
                nx = x + dx[d]
                ny = y + dy[d]
                nz = z + dz[d]

                if 0 <= nz < H and 0 <= nx < X and 0 <= ny < Y and tomato[nz][nx][ny] == 0:
                    tomato[nz][nx][ny] = 1
                    zero -= 1
                    rotten.appendleft([nz,nx,ny])
        # print("day:", day, "rotten:", rotten)
        # print(tomato)
        if not rotten:
            if zero > 0:
                return -1
            else:
                return day-1



print(rotting(X,Y,H,0))


            

