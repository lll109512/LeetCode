n = int(input())
ans = []
# lines = [[1,2,3,4],[1,10,100]]
for i in range(n):
    _ = input()
    line = input().strip().split()
    count = 0
    for num in line:
        if num % 4 == 0:
            count += 2
        elif num % 2 == 0:
            count += 1
        if count >= len(line):
            ans.append("Yes")
    ans.append("No")
for p in ans:
    print(p)


# lines = [[1,2,3,4],[1,10,100]]
