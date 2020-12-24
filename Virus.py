import sys

sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "r")
read = sys.stdin.readline

number_of_pc = int(read().rstrip())
number_of_edge = int(read().rstrip())

edges = []
for _ in range(number_of_edge):
    edges.append(list(map(int, read().split())))


matrix = []
for i in range(number_of_pc+1):
    matrix.append([0]*(number_of_pc+1))


for idx in range(len(edges)):
    matrix[edges[idx][0]][edges[idx][1]] = 1
    matrix[edges[idx][1]][edges[idx][0]] = 1


def virus(start):
    global count
    for row in range(1, number_of_pc+1):
        matrix[row][start] = 0
    for col in range(1, number_of_pc+1):
        if matrix[start][col] == 1:
            count += 1
            virus(col)


count = 0
virus(1)
print(count)

# # 로그
print(edges)
print()

for row in matrix:
    print(row)
