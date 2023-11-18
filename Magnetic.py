T=int(input())
for test_case in range(T):
    n=int(input())
    graph=[]
    for i in range(n):
        graph.append(list(map(int,input().split())))
    answer=0
    pan=0
    for i in range(100):
        pan=0
        for j in range(100):
            if graph[j][i] == 1:
                pan=1
            if graph[j][i] == 2:
                if pan==1:
                    answer+=1
                    pan=0
    print("#{} {}".format(test_case,answer))