import collections

class sushi_que:
    def __init__(self):
        self.rear = 3
        self.front = 0
        self.que = None
        self.customer = None

    def init_que(self):
        self.que = [list() for _ in range(self.rear)]
        self.customer = [list() for _ in range(self.rear)]

    def is_empty(self):
        if self.front == self.rear:
            return True
        return False

    def input_sushi(self,now_x,now_name):
        self.que[now_x].append(now_name)
        #print(self.que)

    def input_customer(self,now_x,now_name,need_to_eat):
        self.customer[now_x].append([now_name,need_to_eat])
        #print(self.customer)

    def output_all(self):
        customers = len(sum(self.customer,[]))
        sushies = len(sum(self.que,[]))
        return customers, sushies

    def rotate(self,present_time,now_t):
        need_to_rotate = (now_t - present_time)% self.rear
        tmp_que = [list() for _ in range(self.rear)]
        for i in range(self.rear):
            tmp_que[(i+need_to_rotate)%self.rear] = self.que[i]
        self.que = tmp_que

    def eating(self):
        for r in range(self.rear):
            for c in range(len(self.customer[r])):
                customer_name = self.customer[r][c][0]
                customer_eat = self.customer[r][c][1]
                cnt = []
                if customer_name in self.que[r] and customer_eat>0:
                    all_sushi = self.que[r].count(customer_name)
                    if self.customer[r][c][1] >= all_sushi:
                        self.customer[r][c][1]-=all_sushi
                        for _ in range(all_sushi):
                            self.que[r].remove(customer_name)
                    else:
                        self.customer[r][c][1] = 0
                        for _ in range(customer_eat):
                            self.que[r].remove(customer_name)
                    cnt.append(customer_name)

                if self.customer[r][c][1]<1:
                    self.customer[r].remove(self.customer[r][c])



l,q = list(map(int,input().split()))
sushi_list = sushi_que()
sushi_list.rear = l
sushi_list.init_que()
present_time = 0
for _ in range(q):
    order = input().split()
    now_t = int(order[1])
    if present_time!=0:
        sushi_list.rotate(present_time,now_t)

    if int(order[0])== 100:
        now_x, now_name = int(order[2]), order[3]
        sushi_list.input_sushi(now_x,now_name)
        sushi_list.eating()
        present_time = now_t

    elif int(order[0])== 200:
        now_x, now_name,need_eat = int(order[2]), order[3], int(order[4])
        sushi_list.input_customer(now_x, now_name,need_eat)
        sushi_list.eating()
        present_time = now_t

    else:
        sushi_list.eating()
        present_time = now_t
        customers, sushies = sushi_list.output_all()
        print(customers,sushies,end=" ")
        print("")