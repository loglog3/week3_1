import sys
import copy
from collections import deque

sys.stdin = open("input.txt", "r")

end_x, end_y = map(int, sys.stdin.readline().split())

ary = []

for _ in range(end_x) :
	ary.append(list(map(int, sys.stdin.readline().strip())))

print(ary)