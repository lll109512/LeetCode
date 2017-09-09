import itertools
# n = int(input())
n = 100
ans = pow(n,2)
itr = itertools.combinations_with_replacement(range(1,n+1),2)

for i,j in itr:
    a,b = i
    c,d = j
    if pow(a,b) == pow(c,d):
        ans += 2
print(ans%1000000007)
