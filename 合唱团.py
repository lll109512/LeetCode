# N = int(input())
# line = input().split()
# line = [int(x) for x in line]
# k,d = input().split()
# k,d = int(k),int(d)
line = [7,-15,31, 49, -44, 35, 44, -47, -23, 15, -11, 10, -21, 10,
    -13, 0, -20, -36, 22, -13, -39, -39, -31, -13, -27, -43, -6,
    40, 5, -47, 35, -8, 24, -31, -24, -1]
k,d = 3,31
maxmin = [[[0]*2 for _ in range(len(line))] for _ in range(k+1)]
for i in range(len(line)):
    for k_p in range(1,k):
        maxmin[0][i][0],maxmin[0][i][1] = line[i],line[i]
        
        for



for x in maxl:
    print(x)
