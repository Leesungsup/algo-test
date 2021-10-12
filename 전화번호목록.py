def solution1(phone_book):
    answer = True
    phone_book.sort()
    print(phone_book)
    for i in range(len(phone_book)-1):
        if phone_book[i+1].find(phone_book[i])==0:
            answer=False
            return answer
    return answer
phone_book=list(map(str,input().split()))
dv=solution1(phone_book)