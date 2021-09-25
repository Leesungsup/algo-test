def quick(array,start,end):
    if start>=end:
        return array
    pivot=start
    left=start+1
    right=end
    while left<=right:
        while left<=end and array[left]<=array[pivot]:
            left+=1
        while right>start and array[right]>=array[pivot]:
            right-=1
        if left>right:
            array[right],array[pivot]=array[pivot],array[right]
        else:
            array[left],array[right]=array[right],array[left]
    quick(array,start,right-1)
    quick(array,right+1,end)
    return array

def solution(array, commands):
    answer = []
    array1=[]
    for i in commands:
        array1=array[i[0]-1:i[1]]
        array1.sort()
        answer.append(array1[i[2]-1])
    return answer

def solution(array, commands):
    answer = []
    array1=[]
    for i in array:
        array1.append(i)
    print(array1)
    for i in commands:
        quick(array,i[0]-1,i[1]-1)
        answer.append(array[(i[0]-1)+(i[2]-1)])
        array=array1
    print(answer)
array=list(map(int,input().split()))
n=int(input())
commands=[]
for i in range(n):
    commands.append(list(map(int,input().split())))
solution(array,commands)
