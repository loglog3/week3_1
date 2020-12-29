# 인접리스트 : 나만의 이해: 배열안에 배열을 넣어 관련된 것들을 정리해놓은 리스트

import sys
sys.setrecursionlimit(10**9)
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline
n = int(input())

parents = [None] + [None] * n


def DFS(i, tree, parent):
    if not parents[i]: #해당 인덱스에 부모가 비어있으면
        parents[i] = parent #인덱스에 부모 넣어준다 
        # 해당하는 리스트 안에 다른 인접한 것들을 하나씩 꺼내서 DFS를 돌린다
        for j in tree[i]:
            # 해당하는 리스트 안에 다른 인접한 것들을 하나씩 꺼내서
            # DFS를 돌릴 경우, 자기 자신이 들어가는 경우가 있는데, 이 경우에는 이미
            # parent[i] 가 설정되어있으므로, 아무 수정없이 return 이 이루어진다.
            # 연결리스트처럼, 타고타고 들어가면서 계속 연결되어 완성되는 형태
            DFS(j, tree, i)
    return


def solution(n):
    # 인접 리스트 생성
    # 배열 안에 배열 형태를 띄는 arr 인접 리스트
    arr = [None] + [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = list(map(int, input().split()))
        arr[a].append(b)
        arr[b].append(a)
    DFS(1, arr, 1)
    return '\n'.join(map(str, parents[2:]))


print(solution(n))
