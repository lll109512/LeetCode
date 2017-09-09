import re
import operator
IN = input()
first, num3 = IN.split("=")
num1 ,num2 = re.split('\+|\-', first)
if '+' in IN:
    op = '+'
else:
    op = '-'

words1 = set()
for i in num1:
    if i.isalpha():
        words1.add(i)
words2 = set()
for i in num2:
    if i.isalpha():
        words2.add(i)
i = len(num1)-1
j = len(num2)-1
k = len(num3)-1
word_dict = {}
un_solov = []
c = 0
while i >= 0 and j >=0:
    if num1[i].isalpha() or num2[j].isalpha():
        if num1[i].isalpha() and num2[j].isalpha():
            if num1[i] == num2[j]:
                if op == '+':
                    num = (int(num3[k])-c)/2
                    word_dict[num1[i]] = num
                    c = 0
            else:
                un_solov.append([num1[i],num2[j],num3[k]])
        elif num1[i].isalpha():
            if num1[i] not in word_dict:
                if op == '+':
                     num = (int(num3[k])-c) - int(num2[j])
                     if num < 0:
                         num = (int('1'+num3[k])-c) - int(num2[j])
                         c = 1
                     else:
                         c = 0
                     word_dict[num1[i]] = num
                else:
                    num = int(num3[k]) + int(num2[j])
                    if num >= 10:
                        num -= 10
                        c = 1
                    else:
                        c = 0
                    word_dict[num1[i]] = num


        else:
            if num2[j] not in word_dict:
                if op == '+':
                     num = (int(num3[k])-c) - int(num1[i])
                     c = 0
                     if num < 0:
                         num = (int('1'+num3[k])-c) - int(num1[i])
                         c = 1
                     else:
                         c = 0
                     word_dict[num2[j]] = num
                else:
                    num = (int(num1[i])-c) - int(num3[k])
                    if num < 0:
                        num = (int('1'+num1[i])-c) - int(num3[k])
                        c = 1
                    else:
                        c = 0
                    word_dict[num2[j]] = num

    i-=1
    j-=1
    k-=1
    if k < 0:
        break

print(un_solov)

for key in sorted(word_dict.keys()):
    print("{} {}".format(key,word_dict[key]))
