import sys
from collections import deque

sys.stdin = open("input.txt", "r")

nbr_cnt, line_cnt, start_nbr = map(int, sys.stdin.readline().split())

line_ary = []

for _ in range(line_cnt) :
	tmp = list(map(int, sys.stdin.readline().split()))
	line_ary.append(tmp)
	tmp2 = list(tmp)
	tmp2.reverse()
	line_ary.append(tmp2)

line_ary.sort()

bfs_ary = [[0] * (nbr_cnt+1) for _ in range(nbr_cnt+1)]

for i in range(len(line_ary)) :
	bfs_ary[line_ary[i][0]][line_ary[i][1]] = 1

dfs_ary=list(bfs_ary)

for i in range(len(bfs_ary)) :
	print(bfs_ary[i])


def dfs(start_nbr : int) :
	print(start_nbr, end='')
	for i in range(1, nbr_cnt + 1) :
		if dfs_ary[start_nbr][i] == 1 :
			for j in range(i, nbr_cnt + 1) :
				dfs_ary[start_nbr][j] = 0
			dfs(i)

dfs(start_nbr)

