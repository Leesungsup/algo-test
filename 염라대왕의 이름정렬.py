T=int(input())
for test_case in range(1,T+1):
    n=int(input())
    names = [input() for _ in range(n)]
    names = list(set(names))
    a=sorted(names, key=lambda x:(len(x),x))
    print("#{}".format(test_case))
    for name in a:
        print(name)
T=int(input())
for test_case in range(1,T+1):
    n=int(input())
    arr=dict()
    for i in range(n):
        s=input()
        if len(s) in arr:
            arr[len(s)].append(s)
        else:
            arr[len(s)]=[s]
    print("#{}".format(test_case))
    for i in arr.keys():
        arr[i].sort()
        for j in set(arr[i]):
            print(j)