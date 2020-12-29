import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt","r")


origin = []
N = int(sys.stdin.readline().rstrip())
for n in range(N-1):
    a, b = map(int,sys.stdin.readline().split())
    origin.append([a,b])
    origin.append([b,a])

route = defaultdict(set)
for key, value in origin:
    route[key].add(value)

answer = [0]*(N+1)

def start(key):
    cand = route[key]
    for i in cand:
        answer[i] = key
        DFS(i, key)
    
    for i in range(2,N+1):
        print(answer[i])

def DFS(key, former_key):
    cand = route[key]
    cand.remove(former_key)
    if len(cand) > 0:
        for i in cand:
            answer[i] = key
            DFS(i, key)

start(1)

    

