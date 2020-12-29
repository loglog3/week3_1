import sys
# from collections import deque

sys.stdin = open("input.txt","r")

R, C = map(int,sys.stdin.readline().split())

A = [list(str(sys.stdin.readline().rstrip())) for r in range(R)]
x = 0
y = 0
save = [A[x][y]]
cnt = 1
max_cnt = 1
dx = [-1,0,1,0]
dy = [0,1,0,-1]


def pathfinder(R,C,x,y,cnt,max_cnt):
    # print("x:",x,"y:",y, "list:", save)
    
    old_letter = A[x][y]
    A[x][y] = False

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        # 경계선
        if -1 < nx and nx < R and -1 < ny and ny < R and A[nx][ny] != False and A[nx][ny] not in save:
            # 있으면 
            save.append(A[nx][ny])
            cnt += 1
            max_cnt = max(cnt, pathfinder(R,C,nx,ny,cnt,max_cnt))
            cnt -= 1
            save.pop()
    A[x][y] = old_letter
    return max_cnt

print(pathfinder(R,C,x,y,cnt,max_cnt))