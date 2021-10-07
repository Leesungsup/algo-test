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
