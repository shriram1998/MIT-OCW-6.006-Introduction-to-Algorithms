import sys

str = ["This", "is", "an", "example", "of", "text", "justification."]
ln = len(str)

cMat = [[sys.maxsize for _ in range(ln)]for _ in range(ln)]
DP = [0 for _ in range(ln+1)]  # Since DP[len]=0
# Required output-> min j in recurrence relation
pos = [None for _ in range(ln)]

pageW = 16


def DPFn(i):
    minPos = i+1
    minCost = DP[i+1]+cMat[i][i]
    for j in range(i+1, ln+1):
        cost = DP[j]+cMat[i][j-1]
        if cost < minCost:
            minCost = cost
            minPos = j
    DP[i] = minCost
    pos[i] = minPos


for i in range(ln-1, -1, -1):
    for j in range(ln-1, i-1, -1):
        line = str[i]
        for k in range(i, j):
            line += ' '+str[k+1]
        cost = pageW-len(line)
        cMat[i][j] = cost**2 if cost >= 0 else sys.maxsize
    DPFn(i)
DP = DP[:-1]

i = 0
while i < ln:
    opStr = ''
    for k in range(i, pos[i]):
        opStr += str[k]+' '
    i = k+1
    print(opStr)
