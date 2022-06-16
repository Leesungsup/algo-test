T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n=int(input())
    arr=list(map(int,input().split()))
    d=dict()
    for i in arr:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    sorted_dict = sorted(d.items(), key = lambda item: item[1], reverse = True)
    binma=sorted_dict[0]
    for i in range(len(sorted_dict)):
        if sorted_dict[i][1]==binma[1]:
            if sorted_dict[i][0]>binma[0]:
                binma=sorted_dict[i]
        else:
            break
    print("#{} {}".format(test_case,binma[0]))
    # ///////////////////////////////////////////////////////////////////////////////////
