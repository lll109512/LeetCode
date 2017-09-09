x = [7,13,15]
k = 6
mid = pow(2,k-1)
while True:
    k = k-1
    if all(num > mid for num in x):
        mid += pow(2,k-1)
    elif all(num < mid for num in x):
        mid -= pow(2,k-1)
    else:
        print(mid)
        break
