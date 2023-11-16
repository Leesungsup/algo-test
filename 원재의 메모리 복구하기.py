T=int(input())
for test_case in range(T):
    n=int(input())
    answer=0
    mem=list(map(int,input()))
    bit=0
    for i in range(len(mem)):
        if mem[i]!=bit:
            answer+=1
            bit=mem[i]
    print("#{} {}".format(test_case,answer))