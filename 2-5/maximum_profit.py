import sys
MAX  = 20000
R = [6,5,4,1,3,4,3]

maxv = -1 * (10**9) - 1
minv = R[0]

for i in range(len(R)):
    maxv = max(maxv, (R[i] - minv))
    minv = min(minv, R[i])

print(maxv)

