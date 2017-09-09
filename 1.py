DATA = []
while(1):
    try:
        IN = input()
        DATA.append(int(IN))
    except EOFError as e:
        break
OUTPUT = []
for num in DATA:
    drink = 0
    bottle = num
    drink_turn = 0
    while(True):
        # print(drink,bottle)
        drink_turn = bottle//3
        bottle = drink_turn + bottle%3
        drink += drink_turn
        if (bottle == 3):
            drink+=1
            break
        elif(bottle == 2 ):
            drink+=1
            break
    OUTPUT.append(drink)

for i in OUTPUT:
    print(i)
