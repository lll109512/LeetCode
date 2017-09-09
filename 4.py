from copy import deepcopy

# N,M,P = input().split()
# N,M,P = int(N),int(M),int(P)
# maze =[]
# for _ in range(int(N)):
#     line = input().split()
#     line = [int(x) for x in line]
#     maze.append(line)
N,M,P = 5,8,100
maze = [
[1,0,0,0,1,0,0,1],
[1,1,0,1,1,1,0,1],
[0,1,0,1,0,1,0,1],
[0,1,1,1,0,1,0,1],
[1,0,0,0,1,1,1,1]
]
Path_table = []
def find(maze,position,P,Path):
    i,j = position
    # print(Path)
    if P < 0:
        return
    if position == (0,M-1):
        Path_table.append(Path)
        return
    if j+1 < M and maze[i][j+1] == 1 and [i,j+1] not in Path:
        print(Path)
        cp2 = deepcopy(Path)
        cp2.append([i,j+1])
        find(maze,(i,j+1),P-1,cp2)
    if i+1 < N and maze[i+1][j] == 1 and [i+1,j] not in Path:
        cp1 = deepcopy(Path)
        cp1.append([i+1,j])
        find(maze,(i+1,j),P,cp1)
    if i-1>= 0 and maze[i-1][j] == 1 and [i-1,j] not in Path:
        cp3 = deepcopy(Path)
        cp3.append([i-1,j])
        find(maze,(i-1,j),P-3,cp3)
    if j-1>= 0 and maze[i][j-1] == 1 and [i,j-1] not in Path:
        cp4 = deepcopy(Path)
        cp4.append([i,j-1])
        find(maze,(i,j-1),P-1,cp4)

find(maze,(0,0),P,[[0,0]])
if len(Path_table) == 0:
    print("Can not escape!")
else:
    result = ''
    for item in min(Path_table,key=lambda x:len(x)):
        result += '[{0},{1}],'.format(item[0],item[1])
    print(result.strip(','))
