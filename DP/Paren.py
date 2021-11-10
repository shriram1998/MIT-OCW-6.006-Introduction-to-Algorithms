import sys
p = [5, 4, 6, 2, 7]
n = 5
m = [[0 for _ in range(n)] for _ in range(n)]
s = [[0 for _ in range(n)] for _ in range(n)]

for d in range(1, n-1):
    for i in range(1, n-d):
        j = i+d
        min = sys.maxsize
        for k in range(i, j):
            val = m[i][k]+m[k+1][j]+(p[i-1]*p[k]*p[j])
            if val < min:
                min = val
                s[i][j] = k
        m[i][j] = min
