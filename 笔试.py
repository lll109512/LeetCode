# INPUT = raw_input().strip()
# id = int(INPUT)
id = 10000000
counter = id
n = 1
while counter > n:
    counter -= n
    n+=1
    id = n
result = ''
i=1
# print(id,counter)
while i <= id:
    # print(result)
    if len(str(i))==1:
        result = result+str(i)
        i+=1
    elif len(str(i))>1:
        result = result+str(i)
        i+=1
print(result[:counter][-1])
