number_of_input = input()
number_list = []
for _ in range(int(number_of_input)):
    x = input()
    number_list.append(int(x))

result = sorted(list(set(number_list)))

for line in result:
    print(line)
