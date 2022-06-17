T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n=int(input())
    arr=[[0]*n for _ in range(n)]
    k=0
    m=n
    x=0
    y=-1
    di=1
    for i in range(n):
        for j in range(m):
            k+=1
            y+=di
            arr[x][y]=k
        m-=1
        for j in range(m):
            k+=1
            x+=di
            arr[x][y]=k
        di*=-1
    print("#{}".format(test_case))
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=' ')
        print()
    # ///////////////////////////////////////////////////////////////////////////////////
