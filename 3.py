INPUT = []
while(True):
    try:
        x = input()
        INPUT.append(x)
    except EOFError as e:
        break

for num in INPUT:
    print(int(num,16))
