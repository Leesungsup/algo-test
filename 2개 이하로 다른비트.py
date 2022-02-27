def binary(number):
    con=''
    while number // 2 >= 1:
        remain = number % 2
        #print(remain)
        number = number // 2
        #print(number)
        con = str(remain) + con
        if number < 2 :
            con = str(number) + con
    return con
def solution(numbers):
    answer = []
    for i in numbers:
        print(bin(i))
        k=bin(i)
        a='0'+k[2:]
        print(a)
        idx=a.rfind('0')
        b=list(a)
        b[idx]='1'
        if i%2!=0:
            b[idx+1]='0'
        print(b)
        answer.append(int(''.join(b), 2))
        c=binary(i)
        print(c)
    print(answer)
    return answer
solution([2,7])
