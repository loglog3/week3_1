import sys
from collections import deque

sys.stdin = open("input.txt", "r")

R, C = map(int,sys.stdin.readline().split())

forest= []
check_water = deque([])
check_hedgedog = deque([])
minute = 1

for r in range(R):
    temp = list(str(sys.stdin.readline().rstrip()))
    forest.append(temp)
    if "*" in temp:
        check_water.append([r,temp.index("*"), minute])
    if "S" in temp:
        check_hedgedog.append([r,temp.index("S"), minute])

dx = [-1,0,1,0]
dy = [0,1,0,-1]


while check_hedgedog:
    while check_water and check_water[0][2] == minute:
        water_node = check_water.popleft()
        water_x = water_node[0]
        water_y = water_node[1]
        
        for d in range(4):
            water_nx = water_x + dx[d]
            water_ny = water_y + dy[d]

            if 0 <= water_nx < R and 0 <= water_ny < C:
                if forest[water_nx][water_ny] == "." or forest[water_nx][water_ny] == "S":
                    check_water.append([water_nx,water_ny, minute+1])
                    forest[water_nx][water_ny] = "*"



    while check_hedgedog and check_hedgedog[0][2] == minute:
        hedgedog_node = check_hedgedog.popleft()
        hedgedog_x = hedgedog_node[0]
        hedgedog_y = hedgedog_node[1]
        
        for d in range(4):
            hedgedog_nx = hedgedog_x + dx[d]
            hedgedog_ny = hedgedog_y + dy[d]

            if 0 <= hedgedog_nx < R and 0 <= hedgedog_ny < C:
                if forest[hedgedog_nx][hedgedog_ny] == "D":
                    print(hedgedog_node[2])
                    exit()
                elif forest[hedgedog_nx][hedgedog_ny] == "." :
                    check_hedgedog.append([hedgedog_nx,hedgedog_ny,hedgedog_node[2]+1])
                    forest[hedgedog_nx][hedgedog_ny] = "S"
        
    minute += 1

print("KAKTUS")