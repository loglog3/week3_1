import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

n, m= map(int, sys.stdin.readline().rstrip().split())
maze = [sys.stdin.readline().rstrip() for _ in range(n)]
visited = [[0] * m for _ in range(n)]
count= 1

#좌/우/하/상
dx=[-1,1,0,0]
dy=[0,0,1,-1]

for i in range(n):
    print(visited[i])

for i in range(n):
    print(maze[i])

print(maze)

def findMaze(x,y):              #좌상단이 0,0 우상단이 x,0 좌하단이 0,y 우하단이 x,y라고 생각했습니다.
    global count
    visited[y][x] = count
    while True:
		
        for i in range(4):
            a= x+dx[i]
            b= y+dy[i]
            if 0<= a < n and 0<= b < m and maze[b][a]=="1":
                visited[b][a] = count +1
                x=a
                y=b
        if a==n-1 and b==m-1 :
            break
    return count
print(findMaze(0,0))