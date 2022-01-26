def convert(number):
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
def solution(n):
    answer = 0
    number=n
    con=''
    con=convert(number)
    #print(con)
    num=0
    for i in con:
        if i=='1':
            num+=1
    while True:
        con=''
        number+=1
        con=convert(number)
        #print(con)
        k=0
        for i in con:
            if i=='1':
                k+=1
        #print(k)
        if num==k:
            answer=number
            break
    return answer
solution(78)
