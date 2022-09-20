def manhattan_distance(A,B):
    distance=0
    for i in range(len(A)):
        distance+=abs(A[i]-B[i])
    return distance
def euclidean_distance(A,B):
    distance=0
    for i in range(len(A)):
        distance+=(A[i]-B[i])**2
    return distance**0.5
d1=[[7,6],
    [2,6],
    [3,8],
    [8,5]
    ]
eu=[]
eu1=[]
eu_C=[]
eu_C1=[]
for i in range(len(d1)):
    eu.append(euclidean_distance(d1[0],d1[i]))
    print(euclidean_distance(d1[0],d1[i]))
print("00000000000000000000000")
for i in range(len(d1)):
    eu1.append(euclidean_distance(d1[1],d1[i]))
    print(euclidean_distance(d1[1],d1[i]))
print("eu",eu)
print("eu1",eu1)
for i in range(len(eu)):
    if eu[i]<eu1[i]:
        eu_C.append(eu[i])
    elif eu[i]>eu1[i]:
        eu_C1.append(eu1[i])
print("eu_C",eu_C)
print("eu_C1",eu_C1)
for i in range(len(d1)):
    print(euclidean_distance([0,0],d1[i]))
print("==============")
for i in range(len(d1)):
    print(euclidean_distance([0,0],d1[i]))
d=[[7,6],
   [2,6],
   [3,8],
   [8,5],
   [7,4],
   [4,7],
   [6,2],
   [7,3],
   [6,4],
   [3,4]]
sum=0
k=[]
k1=[]
C1=[]
C2=[]
sum1=0
for i in range(len(d1)):
    k.append(manhattan_distance(d1[0],d1[i]))
    k1.append(manhattan_distance(d1[1],d1[i]))
    print(manhattan_distance(d1[0],d1[i]))
print("k",k)
print("k1",k1)
for i in range(len(k)):
    if k[i]<k1[i]:
        C1.append(k[i])
        sum+=k[i]
    elif k[i]>k1[i]:
        C2.append(k1[i])
        sum1+=k1[i]
print("C1",C1,sum)
print("C2",C2,sum1)
