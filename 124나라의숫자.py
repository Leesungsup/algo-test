def solution2(n):
    k=bin(n)
    print(n)
    save = []
    while True:
        a = int(n / 2)
        b = int(n % 2)
        save.insert(0, b)
        if a != 0:
            n = a
        else:
            break
    final = ''.join(map(str, save))
    print(final)
def solution1(n):
    answer=''
    while n:
        if n%3:
            answer+=str(n%3)
            n//=3
        else:
            answer+='4'
            n=n//3-1
    return answer[::-1]
def solution(n):
    answer = ''
    while n:
        if n % 3:
            answer += str(n % 3)
            n //= 3
        else:
            answer += "4"
            n = n//3 - 1
    return answer[::-1]
def convert():
    number=int(input())
    num=int(input())
    answer=''
    while number//num>=1:
        result=number%num
        number=number//num
        answer=str(result)+answer
        if number<num:
            answer=str(number)+answer