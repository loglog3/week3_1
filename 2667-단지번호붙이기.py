import sys
import copy
sys.stdin = open("input.txt","r")


N = int(sys.stdin.readline().rstrip())
apt = [list(map(int, list(str(sys.stdin.readline().rstrip())))) for _ in range(N)]
# TF = copy.deepcopy(apt)

total = []
name = 1

# DFS에서 cnt 셈 (완료하면 num + 1)
def DFS(x,y):
    global cnt
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < N and 0 <= ny < N and apt[nx][ny] == 1:
            apt[nx][ny] = 0
            cnt += 1
            DFS(nx,ny)
    
    return


# 이중 for문으로 전체 탐색함
for i in range(N):
    for j in range(N):

        # apt에서 1인곳을 만나면 DFS 실행
        if apt[i][j] == 1:
            cnt = 1
            apt[i][j] = 0
            DFS(i,j)
            total.append(cnt)
            name += 1

print(name-1)
total.sort()
for i in total:
    print(i)


# DFS에서 방문할 때마다 TF False로 돌림