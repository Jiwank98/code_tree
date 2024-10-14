import collections

def rotation(r,array,target):
    now_target_array = [[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            now_target_array[i][j] = array[i][j]

    target_x = target[0]-1
    target_y = target[1]-1

    if r==1: #90도회전
        for i in range(3):
            for j in range(3):
                now_target_array[target_y+j][target_x+2-i] = array[target_y+i][target_x+j]

    elif r==2: #180도회전
        for i in range(3):
            for j in range(3):
                now_target_array[target_y+2-i][target_x+2-j] = array[target_y+i][target_x+j]

    else: #270도회전
        for i in range(3):
            for j in range(3):
                now_target_array[target_y+2-j][target_x+i] = array[target_y+i][target_x+j]

    return now_target_array

def BFS(array):#BFS로 배열에 인접한 애들 다 지나기
    score = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visited = [[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if visited[i][j] ==0:
                que = collections.deque()
                trace = collections.deque()
                que.append([i,j])
                trace.append([i,j])
                visited[i][j] = 1
                wanted_value = array[i][j]
                while que:
                    now_xy = que.popleft()
                    now_y, now_x = now_xy[0],now_xy[1]
                    for rotate in range(4):
                        if checkrange(now_x + dx[rotate], now_y + dy[rotate]):
                            next_xy = array[now_y+dy[rotate]][now_x+dx[rotate]]
                            if visited[now_y+dy[rotate]][now_x+dx[rotate]]==0 and next_xy==wanted_value:
                                que.append([now_y+dy[rotate],now_x+dx[rotate]])
                                visited[now_y+dy[rotate]][now_x+dx[rotate]]=1
                                trace.append([now_y+dy[rotate],now_x+dx[rotate]])
                if len(trace)>2:
                    score+=len(trace)
                    while trace:
                        tr = trace.popleft()
                        array[tr[0]][tr[1]] = 0
    return score

#fill 확인 요망 (10/9)
def fill(array,num_inputs):
    for j in range(5):
        for i in range(4,-1,-1):
            if array[i][j] ==0:
                x = num_inputs.popleft()
                array[i][j] = x
    return array




def checkrange(x, y):
    return 0<= x < 5 and 0<= y <5



k,m = input().split(" ")
k,m = int(k),int(m)
array = [[0]*5 for _ in range(5)]
for i in range(5):
    num_line = input().split(" ")
    for j in range(5):
        array[i][j] = int(num_line[j])
num_inputs = list(map(int,input().split()))
num_inputs = collections.deque(num_inputs)


for _ in range(k):
    max_value = 0
    max_array = None

    for rotate_num in range(1,4):
        for i in range(1,4):
            for j in range(1,4):
                target = [i, j]
                target_array = rotation(rotate_num, array, target)
                now_score = BFS(target_array)
                if max_value < now_score:
                    max_value = now_score
                    max_array = target_array

    if max_array is None:
        break
    array = max_array

    while True:
        array = fill(array,num_inputs)
        new_score = BFS(array)
        if new_score ==0:
            break
        max_value+=new_score

    print(max_value,end=" ")