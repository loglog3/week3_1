# # # 참고함
# Dynamic Programming 활용한 풀이

n, k = (int, input().split())
# 코인 정렬해줘야한다
coin = sorted(list(set(int(input()) for _ in range(n))))
# 초기 배열은 '목표금액+1' 로 채워준다. '1원으로 가득 채울 때 드는 동전의 갯수'+1 이다
dp = [20000] * (k+1)
# 0원을 만드는데 드는 코인은 0개이다.
dp[0] = 0


for i in range(1, k+1):
    for c in coin:
        if i-c < 0:
            break
        # dp[i-c]+1은  i-c까지의 최적해에 마지막 C동전을 사용하는 것을 나타냄,
        dp[i] = min(dp[i-c]+1, dp[i])
        # 이에따라 dp[i-c]+1 만큼의 코인을 사용하게 된다.
# 최적해가 없다 == 리스트값이 20000이다 => 이러면 -1을 출력한다
print(dp[k] if dp[k] != 20000 else -1)


# import sys
# # # # fail
# sys.setrecursionlimit(10**9)
# sys.stdin = open("input.txt", "r")
# read = sys.stdin.readline

# coins, N = list(map(int, read().rstrip().split()))
# coin = []
# origin = N
# tmp = 0
# count = []
# for _ in range(coins):
#     coin.append(int(read()))
# coin = list(set(coin))
# coin.sort()
# coins = len(coin)

# for b in range(coins-1, -1, -1):
#     for s in range(b, -1, -1):
#         cnt = N // coin[s]
#         rest = N % coin[s]
#         tmp += cnt
#         N = rest
#         if rest == 0:
#             count.append(tmp)

#     N = origin
#     tmp = 0

# if not count:
#     count.append(-1)
# print(min(count))

# # 2 10
# # 2
# # 3

# # 큰 값부터 넣어보기
# # 구하고자하는 값보다 주어진 동전이 더 클 경우
