# IN = input()
def LCS(x, y):
    if (len(x) == 0 or len(y) == 0):
        return 0
    else:
        a = x[0]
        b = y[0]
        if (a == b):
            return LCS(x[1:], y[1:])+1
        else:
            return cxMax(LCS(x[1:], y), LCS(x, y[1:] )  )

def cxMax(a, b):
    if (a>=b):
        return a
    else:
        return b


def sub_p(cur_len):
    global case
    if cur_len == length//2:
        return
    if cur_len == 0:
        case.add("()")
        sub_p(cur_len+1)
    else:
        new_set = set()
        for b in case:
            new_set.add(b+"()")
            new_set.add("()"+b)
            new_set.add("("+b+")")
        case = new_set
        sub_p(cur_len+1)


IN = "(((())()()))"
length = len(IN)
case = set()
sub_p(0)
case = list(case)
case.remove(IN)
# for i in case:
#     print(i)

ans = 0
c_m = 0
for line in case:
    m = LCS(IN,line)
    if m > c_m:
        ans = 1
        c_m = m
    elif m == c_m:
        ans += 1

print(ans)
