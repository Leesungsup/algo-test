def convert(number,n):
    con=''
    print(number,n)
    while number // n >= 1:
        remain = number % n
        print(remain)
        number = number // n
        print(number)
        con = str(remain) + con
        if number < n :
            con = str(number) + con
    return con
def convert1(n, q):
    rev_base = ''
    if n==0:
        return '0'
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    return rev_base[::-1]
def convert_notation(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    return convert_notation(q, base) + T[r] if q else T[r]

def solution(n, t, m, p):
    answer = ''
    arr=['']*(m+1)
    #print(arr)
    sun=0
    i=-1
    #print(t)
    b=0
    while True:
        i+=1
        #print(i)
        k=convert_notation(i,n)
        #print(k)
        for j in k:
            arr[(sun%m)+1]+=j
            if len(arr[p])==t:
                b=1
                break
            sun+=1
        if b==1:
            break
    #print(arr)
    return arr[p]
solution(2,4,2,1)
