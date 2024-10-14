import collections


def check1(maps,place_x,place_y,real_row,side):
    now_x = [place_x]
    now_y = [place_y]
    def _check1(maps,place_x,real_row,side):
        if now_y[0]+2<=real_row-1:
            if maps[now_y[0]+2][place_x]==0 and maps[now_y[0]+1][place_x-1]==0 and maps[now_y[0]+1][place_x+1]==0:
                now_y[0]+=1
                _check1(maps, place_x, real_row,side)
            else:
                return now_x[0],now_y[0]
        else:
            return now_x[0], now_y[0]
    _check1(maps, place_x, real_row,side)
    return now_x[0],now_y[0]


def check2(maps,place_x,place_y,real_row,side):
    now_x = [place_x]
    now_y = [place_y]
    now_side = [side]
    def _check2(maps,real_row):
        if now_x[0]-2>=0 and now_y[0]+2 <= real_row -1:
            if maps[now_y[0]][now_x[0]-2]==0 and maps[now_y[0]+1][now_x[0]-1]==0 and maps[now_y[0]-1][now_x[0]-1]==0 and maps[now_y[0]+1][now_x[0]-2]==0 and maps[now_y[0]+2][now_x[0]-1]==0:
                now_x[0]-=1
                now_y[0]+=1
                if now_side[0]==0:
                    now_side[0] = 3
                else:
                    now_side[0]-=1
                _check2(maps,real_row)
            else:
                return now_x[0],now_y[0], now_side[0]
        else:
            return now_x[0], now_y[0], now_side[0]

    _check2(maps,real_row)
    return now_x[0], now_y[0], now_side[0]


def check3(maps,place_x,place_y,real_row,side):
    now_x = [place_x]
    now_y = [place_y]
    now_side = [side]
    def _check3(maps,real_row):
        if now_x[0]+2<=column-1 and now_y[0]+2 <= real_row -1:
            if maps[now_y[0]][now_x[0]+2]==0 and maps[now_y[0]+1][now_x[0]+1]==0 and maps[now_y[0]-1][now_x[0]+1]==0 and maps[now_y[0]+2][now_x[0]+1]==0 and maps[now_y[0]+1][now_x[0]+2]==0:
                now_x[0]+=1
                now_y[0]+=1
                now_side[0]+=1
                now_side[0]%=4
                _check3(maps,real_row)
            else:
                return now_x[0],now_y[0], now_side[0]
        else:
            return now_x[0], now_y[0],  now_side[0]

    _check3(maps,real_row)
    return now_x[0], now_y[0],  now_side[0]


def score(maps,place_x,place_y,side):
    first_exit_x = place_x
    first_exit_y = place_y
    new_maps = [[0]* len(maps[0]) for _ in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            new_maps[i][j]+=maps[i][j]

    if 0<=first_exit_y<=3 or first_exit_x==0 or first_exit_x == len(maps[0])-1:
        return 0, new_maps
    first_side = side
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    #0 : 동, 1: 서, 2: 북  3: 남
    for i in range(4):
        if maps[place_y+dy[i]][place_x+dx[i]] == 2 :
            first_exit_y= place_y+dy[i]
            first_exit_x = place_x+dx[i]

    que = collections.deque()
    que.append([first_exit_x,first_exit_y,first_side])

    def case(maps,x,y,side): #현재 골렘의 어디 위치에 있는지 찾기(북, 남, 동, 서)
        next_exit_x = x
        next_exit_y = y
        if y<=len(maps)-3 and  1<=x<= len(maps[0])-2 and maps[y+1][x] >= 1 and maps[y + 2][x] >= 1 and maps[y+1][x - 1] >= 1 and maps[y+1][x+1] >= 1:  #북 0

            if maps[y + 2][x] == 2:
                maps[y + 1][x], maps[y + 1][x - 1], maps[y + 1][x + 1] = -1, -1, -1
                next_exit_x, next_exit_y,side = x, y+2,  2
            elif maps[y+1][x - 1] == 2:
                maps[y + 1][x], maps[y + 2][x], maps[y + 1][x + 1] = -1, -1, -1
                next_exit_x, next_exit_y,side = x - 1 , y+1, 3
            elif maps[y+1][x+1] == 2:
                maps[y + 1][x], maps[y + 2][x], maps[y + 1][x - 1] = -1, -1, -1
                next_exit_x, next_exit_y,side = x+1, y + 1 , 1
            else:
                maps[y + 2][x], maps[y + 1][x - 1], maps[y + 1][x + 1] = -1, -1, -1
                next_exit_x, next_exit_y, side = x, y, 0


        elif y>=4 and 1<=x<=len(maps[0])-2 and maps[y-1][x] >= 1 and maps[y-2][x] >= 1 and maps[y - 1][x - 1] >= 1 and maps[y-1][x +1] >= 1:  # 남 2

            if maps[y-2][x] == 2:
                maps[y - 1][x], maps[y - 1][x - 1], maps[y - 1][x + 1] = -1, -1, -1
                next_exit_x, next_exit_y,side = x, y-2, 0
            elif maps[y - 1][x - 1] == 2:
                maps[y - 1][x], maps[y - 2][x], maps[y - 1][x + 1] = -1, -1, -1
                next_exit_x, next_exit_y,side = x - 1 , y-1, 3
            elif maps[y-1][x +1] == 2:
                maps[y - 1][x], maps[y - 2][x], maps[y - 1][x - 1] = -1, -1, -1
                next_exit_x, next_exit_y,side = x + 1 , y-1, 1
            else:
                maps[y - 2][x], maps[y - 1][x - 1], maps[y - 1][x + 1] = -1, -1, -1
                next_exit_x, next_exit_y,side = x,y,2

        elif 5<=y<=len(maps)-2 and x>=2 and  maps[y][x-1]>=1 and maps[y][x-2]>=1 and maps[y-1][x-1] >= 1 and maps[y+1][x-1] >= 1: #동 1
            if maps[y][x-2] == 2:
                maps[y][x - 1], maps[y - 1][x - 1], maps[y + 1][x - 1] = -1, -1, -1
                next_exit_x, next_exit_y,side = x-2, y, 3
            elif maps[y-1][x-1] == 2:
                maps[y][x - 1], maps[y][x - 2], maps[y + 1][x - 1] = -1, -1, -1
                next_exit_x, next_exit_y,side = x - 1 , y-1, 0
            elif maps[y+1][x-1] == 2:
                maps[y][x - 1], maps[y][x - 2], maps[y - 1][x - 1] = -1, -1, -1
                next_exit_x, next_exit_y,side = x - 1 , y+1, 2
            else:
                maps[y][x - 2], maps[y - 1][x - 1], maps[y + 1][x - 1] = -1, -1, -1
                next_exit_x, next_exit_y,side = x,y,1


        elif 5<=y<=len(maps)-2 and x<=len(maps[0])-3 and maps[y][x + 1] >= 1 and maps[y][x + 2] >= 1 and maps[y - 1][x+1] >= 1 and maps[y +1][x+1] >= 1: #서3

            if maps[y][x+2] == 2:
                maps[y][x + 1],  maps[y - 1][x + 1], maps[y + 1][x + 1] = -1, -1, -1
                next_exit_x, next_exit_y,side = x+2, y, 1
            elif maps[y-1][x+1] == 2:
                maps[y][x + 1], maps[y][x + 2], maps[y + 1][x + 1] = -1, -1, -1
                next_exit_x, next_exit_y,side = x + 1 , y-1, 0
            elif maps[y +1][x+1] == 2:
                maps[y][x + 1], maps[y][x + 2], maps[y - 1][x + 1] = -1, -1, -1
                next_exit_x, next_exit_y,side = x + 1 , y+1 , 2
            else:
                maps[y][x + 2], maps[y - 1][x + 1], maps[y + 1][x + 1] = -1, -1, -1
                next_exit_x, next_exit_y,side =x,y,3

        else:
            return next_exit_x, next_exit_y, side

        return next_exit_x,next_exit_y,side

    visited = [[0]* len(maps[0]) for _ in range(len(maps))]
    visited[first_exit_y][first_exit_x] = 1
    next_exit_x, next_exit_y,next_side = first_exit_x, first_exit_y,side

    #가장 밑쪽으로 길찾기 => 1. 현재 출구시작 다음 골렘 이동 BFS /계속 만약 다음 골렘 없으면 (직전 출구랑 갈수있는 유일한 출구가 동일) 현재 위치에서 가장 남쪽으로 반환/ 몸 벗어나 있으면 결과 0 반환
    while que:
        x = que.popleft()
        exit_x, exit_y, exit_side = x[0], x[1], x[2]
        cnt = 0
        if 4<=exit_y+dy[exit_side]<=len(maps)-1 and 0<=exit_x+dx[exit_side]<=len(maps[0])-1 and maps[exit_y+dy[exit_side]][exit_x+dx[exit_side]] == 1:
            cnt+=1
            next_exit_x, next_exit_y,next_side = case(maps,exit_x+dx[exit_side],exit_y+dy[exit_side],next_side)
            if visited[next_exit_y][next_exit_x] !=1:
                visited[next_exit_y][next_exit_x] =1
                que.append([next_exit_x, next_exit_y,next_side])

        if 4<=exit_y+dy[(exit_side+5)%4]<=len(maps)-1 and 0<=exit_x+dx[(exit_side+5)%4]<=len(maps[0])-1 and maps[exit_y+dy[(exit_side+5)%4]][exit_x+dx[(exit_side+5)%4]] == 1 and cnt ==0 :
            cnt+=1
            next_exit_x, next_exit_y, next_side = case(maps, exit_x+dx[(exit_side+5)%4], exit_y+dy[(exit_side+5)%4],next_side)
            if visited[next_exit_y][next_exit_x] != 1:
                visited[next_exit_y][next_exit_x] = 1
                que.append([next_exit_x, next_exit_y, next_side])

        if 4<=exit_y-dy[(exit_side+5)%4]<=len(maps)-1 and 0<=exit_x-dx[(exit_side+5)%4]<=len(maps[0])-1 and maps[exit_y-dy[(exit_side+5)%4]][exit_x-dx[(exit_side+5)%4]] == 1 and cnt ==0:
            next_exit_x, next_exit_y, next_side = case(maps, exit_x-dx[(exit_side+5)%4], exit_y-dy[(exit_side+5)%4],next_side)
            if visited[next_exit_y][next_exit_x] != 1:
                visited[next_exit_y][next_exit_x] = 1
                que.append([next_exit_x, next_exit_y, next_side])
    next_exit_x,next_exit_y,next_side = case(maps,next_exit_x,next_exit_y,next_side)
    if next_side ==1 or next_side == 3:
        next_exit_y+=1
    elif next_side==0:
        next_exit_y += 2
    else:
        next_exit_y+=0

    return next_exit_y-2, new_maps


row, column, k = input().split(" ")
row,column,k = int(row),int(column),int(k)
real_row = row+3
maps = [[0] * column for _ in range(real_row)]

answer = 0
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
#북 : 0  동:1   남:2    서:3

for i in range(k):
    spot, side = input().split(" ") #spot은  첫 열 위치, side는 골렘의 첫 출구 위치
    # 1은 골렘 위치 / 2는 골렘의 출구
    spot, side = int(spot), int(side)
    place_x = spot-1
    place_y = 1
    cnt= False
    #경우의 수는 네개 -> T 1결과로 체인지 / FT -> 2결과로 체인지 / FFT / FFF -> 3결과로 체인지
    #첫번째 남쪽으로 내려가는것 -> 추가 구현 가능 처음일때는 그냥 쭉내리기(가운데열들이라면)
    place_x, place_y = check1(maps,place_x,place_y,real_row,side)
    if place_y==real_row-2: #T
        maps[place_y][place_x] = 1
        maps[place_y + 1][place_x] = 1
        maps[place_y - 1][place_x] = 1
        maps[place_y][place_x - 1] = 1
        maps[place_y][place_x + 1] = 1
        maps[place_y + dy[side]][place_x + dx[side]] = 2

        scores,maps = score(maps, place_x, place_y, side)
        if scores == 0:
            maps = [[0] * column for _ in range(real_row)]
        answer+=scores
        cnt= True

    #두번째 서쪽방향 회전
    if cnt == False:
        place_x, place_y,side = check2(maps,place_x,place_y,real_row,side)
        if place_y==real_row-2:
            maps[place_y][place_x] = 1
            maps[place_y + 1][place_x] = 1
            maps[place_y - 1][place_x] = 1
            maps[place_y][place_x - 1] = 1
            maps[place_y][place_x + 1] = 1
            maps[place_y + dy[side]][place_x + dx[side]] = 2

            scores,maps = score(maps, place_x, place_y, side)
            if scores == 0:
                maps = [[0] * column for _ in range(real_row)]
            answer += scores
            cnt = True


    #세번째 동쪽방향 회전
    if cnt == False:
        place_x, place_y, side = check3(maps, place_x, place_y, real_row, side)
        maps[place_y][place_x] = 1
        maps[place_y + 1][place_x] = 1
        maps[place_y - 1][place_x] = 1
        maps[place_y][place_x - 1] = 1
        maps[place_y][place_x + 1] = 1
        maps[place_y + dy[side]][place_x + dx[side]] = 2

        scores,maps = score(maps, place_x, place_y, side)
        if scores == 0:
            maps = [[0] * column for _ in range(real_row)]

        answer += scores
        if place_y == real_row - 2:
            cnt = True

    #123다안되면 끝내고 리셋
    if 0<=place_y<=3 or place_x==0 or place_x == column-1:
        maps = [[0] * column for _ in range(real_row)]

print(answer)