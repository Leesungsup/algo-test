numbers=list(map(int,input().split()))
array=[]
numb=[]
a=''
array=list(map(str,numbers))
print(array)
numb=sorted(array,key=lambda x:x*3,reverse=True)
print(numb)
a=str(int(''.join(numb)))
print(a)