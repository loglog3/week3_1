import sys
sys.setrecursionlimit(10000)
sys.stdin = open("input.txt", "r")

size = int(input())
paper = []
for i in range(size):
    paper.append(list(map(int, input().split())))

# for i in range(size):
#     print(paper[i])

blueCount = 0
whiteCount = 0


def paperCut(Rowstart, Rowend, Colstart, Colend):
    global blueCount, whiteCount

    if Rowstart > Rowend:
        return

    if Colstart > Colend:
        return

    Rowmiddle = (Rowstart+Rowend)//2
    Colmiddle = (Colstart+Colend)//2

    if Rowstart == Rowend:  # 가장 잘게 쪼개짐
        if paper[Rowstart][Colstart] == 1:
            blueCount += 1
            return
        else:
            whiteCount += 1
            return

    criteria = paper[Rowstart][Colstart]
    for row in range(Rowstart, Rowend):  # 처음부터 끝까지
        for col in range(Colstart, Colend):
            if criteria != paper[row][col]:
                paperCut(Rowstart, Rowmiddle, Colstart, Colmiddle)
                paperCut(Rowstart, Rowmiddle, Colmiddle, Colend)
                paperCut(Rowmiddle, Rowend, Colstart, Colmiddle)
                paperCut(Rowmiddle, Rowend, Colmiddle, Colend)
                return
    if criteria == 1:
        blueCount += 1
        return
    if criteria == 0:
        whiteCount += 1
        return


paperCut(0, size, 0, size)
print(whiteCount)
print(blueCount)
