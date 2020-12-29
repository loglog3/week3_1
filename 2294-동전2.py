import sys
from collections import deque

sys.stdin = open("input.txt","r")

coin = set([])
n, k = map(int,sys.stdin.readline().split())
visit = [False] * (k+1)

for i in range(n):
    new_coin = int(sys.stdin.readline().rstrip())
    if new_coin < k:
        coin.add(new_coin)
        visit[new_coin] = True

coin = sorted(coin)
l = len(coin)
sushi = deque([])

for i in range(l):
    if coin[i] == k:
        print(1)
        exit()
    else:
        sushi.append([coin[i],i])
turn = 1
while sushi:
    for _ in range(len(sushi)):
        temp = sushi.popleft()
        for i in range(temp[1],l):
            new = [temp[0] + coin[i], temp[1]]
            if new[0] == k:
                print(turn+1)
                exit()
            elif new[0] < k:
                if visit[new[0]] == False: 
                    sushi.append(new)
    turn += 1
print(-1)