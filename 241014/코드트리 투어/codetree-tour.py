import heapq
import math

class graph():
    def __init__(self):
        self.cities = {}

    def add_node(self,n):
        for node in range(0,n):
            if node not in self.cities:
                self.cities[node] = {}

    def add_edge(self,information):
        start_node, destination_node, weight = information[0], information[1],information[2]
        if destination_node not in self.cities[start_node]:
            self.cities[start_node][destination_node] = weight
        else:
            self.cities[start_node][destination_node] = min(self.cities[start_node][destination_node],weight)


        if start_node not in self.cities[destination_node]:
            self.cities[destination_node][start_node] =weight
        else:
            self.cities[destination_node][start_node] = min(self.cities[destination_node][start_node], weight)



    def calcualte_value(self,start_root):
        #우선순위 큐 구현하기
        now_time = {node: math.inf for node in self.cities}
        node_original = {node: None for node in self.cities}
        now_time[start_root] = 0
        visited = []
        heap = []
        heapq.heappush(heap,(0,start_root))

        while heap:
            prev_time, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.append(node)

            for adjenct in self.cities[node]:
                weight = self.cities[node][adjenct]
                this_time = prev_time + weight
                if this_time < now_time[adjenct]:
                    now_time[adjenct] = this_time
                    node_original[adjenct] = node
                    heapq.heappush(heap,(now_time[adjenct],adjenct))

        return now_time

class Pakage():
    def __init__(self):
        self.package_id = None
        self.revenue = None
        self.destination_city_id = None
        self.distance = None
        self.profit = None

    def __lt__(self, other):
        if self.profit == other.profit:
            return self.package_id < other.package_id
        return self.profit > other.profit



max_nodes = 2000
MAX_ID = 30005
start_root = [0]
Graph = graph()
now_root = -1
package_heap = []
isMade = [False] * MAX_ID
isCancel = [False] * MAX_ID

Q = int(input())
for i in range(Q):
    order = input().split(" ")
    order_num = int(order[0])

    if order_num==100:
        n,m = int(order[1]),int(order[2])
        Graph.add_node(n)
        for line in range(3,3 + m*3,3): #간선 정보 저장
            v_i , u_i, w_i = int(order[line]), int(order[line+1]), int(order[line+2])
            Graph.add_edge([v_i , u_i, w_i])
        global value_array
        value_array = Graph.calcualte_value(start_root[-1])


    elif order_num==200:
        sell_id, revenue, destination = int(order[1]), int(order[2]), int(order[3])
        package = Pakage()
        package.package_id = sell_id
        package.revenue = revenue
        package.destination_city_id = destination
        package.distance = value_array[package.destination_city_id]
        package.profit = (package.revenue - package.distance)
        heapq.heappush(package_heap,package)
        isMade[sell_id] = True


    elif order_num == 300:
        search_id = int(order[1])
        if isMade[search_id] == True:
            isCancel[search_id] = True


    elif order_num==400:
        cnt = 0
        #start_list보고 먼저 distance랑 revenue 계산해야함
        if now_root != start_root[-1]:
            value_array = Graph.calcualte_value(start_root[-1])
            for now_package in package_heap:
                now_package.distance = value_array[now_package.destination_city_id]
                now_package.profit = (now_package.revenue - now_package.distance)
            now_root = start_root[-1]
            tmp_packages = []
            while package_heap:
                tmp_packages.append(heapq.heappop(package_heap))
            for now_package in tmp_packages:
                heapq.heappush(package_heap, now_package)
                isMade[now_package.package_id] = True

        while package_heap:
            now_best = package_heap[0]
            if now_best.profit < 0:
                break
            heapq.heappop(package_heap)
            if not isCancel[now_best.package_id]:
                cnt+=1
                print(now_best.package_id)
                break
        if cnt ==0:
            print("-1")


    else:
        changed_root = int(order[1])
        start_root.append(changed_root)