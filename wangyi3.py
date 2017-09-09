import collections
line_n = int(input())
uid = []
iid = []
for _ in range(line_n):
    line = input().split()
    line = [int(x) for x in line]
    uid.append(line[1])
    iid.append(line[2])
re_dict = collections.defaultdict(int)
for i in range(line_n):
    if uid[i] in re_dict:
        continue
    count = 0
    l = []
    for j in range(line_n):
        if iid[j] == iid[i] and uid[i] != uid[j]:
            count += 1
            l.append(uid[j])
    if count > 0:
        if uid[i] not in re_dict:
            re_dict[uid[i]] = count
        for k in l:
            if k not in re_dict:
                re_dict[k] = count

for key in sorted(re_dict.keys()):
    print("{} {}".format(key,re_dict[key]))
