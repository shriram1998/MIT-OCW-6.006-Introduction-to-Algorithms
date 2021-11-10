W = [0, 2, 3, 4, 5]  # Weights
P = [0, 1, 2, 5, 6]  # Profits
m = 8  # Max weight that the sack can hold

k = [[0 for _ in range(m+1)] for _ in range(len(P))]  # DP table
R = [0 for _ in range(len(P))]  # Result


for i in range(len(P)):
    for w in range(m+1):
        if i == 0 or w == 0:
            k[i][w] = 0
        elif w >= W[i]:
            k[i][w] = max(P[i]+k[i-1][w-W[i]], k[i-1][w])
            '''
                P[i]+k[i-1][w-W[i]] Consider a new weight and do the sum of suffixes of
                of previous row to new weight afterwards.
            '''
        else:
            k[i][w] = k[i-1][w]

w = m  # check starts from k[n][w]
for i in range(len(P)-1, -1, -1):
    if k[i][w] not in k[i-1]:
        R[i] = 1
        w = w-W[i]

R = R[1:]
print(R)
