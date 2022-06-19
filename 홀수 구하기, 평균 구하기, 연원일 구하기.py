T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    sum=0
    arr=list(map(int,input().split()))
    for i in arr:
        if i%2==1:
            sum+=i
    print("#{} {}".format(test_case,sum))
    # ///////////////////////////////////////////////////////////////////////////////////
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    sum=0
    arr=list(map(int,input().split()))
    for i in arr:
        sum+=i
    print("#{} {}".format(test_case,round(sum/10)))
    # ///////////////////////////////////////////////////////////////////////////////////
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    year=[]
    mon=[]
    day=[]
    a=0
    arr=input()
    for i in range(4):
        year.append(arr[i])
    year1=int(''.join(year))
    for i in range(4,6,1):
        mon.append(arr[i])
    mon1=int(''.join(mon))
    for i in range(6,8,1):
        day.append(arr[i])
    m1=[4,6,9,11]
    m2=[1,3,5,7,8,10,12]
    day1=int(''.join(day))
    if 1<=mon1<=12:
        if mon1 in m1:
            if 1<=day1<=30:
                a=1
        elif mon1 in m2:
            if 1<=day1<=31:
                a=1
        elif mon1==2:
            if 1<=day1<=28:
                a=1
    if a==1:
        print("#{} {}".format(test_case,''.join(year)+'/'+''.join(mon)+'/'+''.join(day)))
    else:
        print("#{} -1".format(test_case))
    # ///////////////////////////////////////////////////////////////////////////////////
