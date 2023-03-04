def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))
def quick(start,end,array):
    if start>=end:
        return array
    pivot=start
    left=start+1
    right=end
    while start<end:
        while array[left]<=array[pivot] and left<=end:
            left+=1
        while array[right]>=array[pivot] and right>start:
            right-=1
        if left>right:
            array[right],array[pivot]=array[pivot],array[right]
        else:
            array[right],array[left]=array[left],array[right]
    quick(right+1,end,array)
    quick(start,right-1,array)
    return array
def solution(array,commands):
    answer=[]
    array1=[]
    for i in commands:
        array1=array[i[0]-1:i[1]]
        array1.sort()
        answer.append(array1[i[2]-1])
    print(answer)
    return answer
def solutions(numbers):
    answer=''
    array=list(map(str,numbers))
    array=sorted(array,key=lambda x:x*3,reverse=True)
    answer=str(int(''.join(array)))
    print(answer)
def solution2(numbers):
    answer=''
    array=list(map(str,numbers))
    array=sorted(array,key=lambda x:x*3,reverse=True)
    answer=str(int(''.join(array)))
    print(answer)
def solution4(array):
    answer=[]
    answer=sorted(array)
    h=len(answer)
    while True:
        num=0
        for i in answer:
            if h<=i:
                num+=1
            if num>=h:
                return h
        h=h-1
def solution(array):
    array1=[]
    array1=sorted(array)
    h=len(array1)
    while True:
        num=0
        for i in array1:
            if h<=i:
                num+=1
            if num>=h:
                return h
        h=h-1

array=list(map(int,input().split()))
commands=list(map(int,input().split()))
solutions(array)
def solution1(array,commands):
    answer=[]
    for i in commands:
        array1=array[i[0]-1:i[1]]
        array1.sort()
        answer.append(array1[i[2]-1])
    print(answer)
    return answer
def solution1(numbers):
    answer=''
    array1=[]
    array=list(map(str,numbers))
    array1=sorted(array,key=lambda x:x*3, reverse=True)
    answer=''.join(array1)
    print(answer)
    return answer
def solution5(array,commands):
    answer=[]
    for i in range(len(commands)):
        array1=array[i[0]-1:i[1]]
        array1.sort()
        answer.append(array1[i[2]])
    return answer
def solutioin6(numbers):
    answer=''
    array=list(map(str,numbers))
    numb=sorted(array,key=lambda x:x*3,reverse=True)
    answer=str(int(''.join(numb)))
    print(array)
    return answer
def solution7(citations):
    answer=0
    array=[]
    array=sorted(citations)
    h=len(array)
    while True:
        num=0
        for i in array:
            if h<=i:
                num+=1
            if num>=h:
                return h
        h=h-1
    return answer