target='ABC'
text='ABABCA'
for i in  range(len(text)-len(target)):
    for j in range(len(target)):
        if text[i+j]==target[j]:
            j+=1
        else:
            break
    print('Indentified')
    break
def BruteForce(p,t):
    i=0
    j=0
    while i<len(t) and j < len(p):
        if t[i]!=p[j]:
            i=i-j
            j=-1
        i+=1
        j+=1
    if j==len(p):
        return i-len(p)
    else:
        return -1
pattern="Python"
text="Hello Python World"
BruteForce(pattern,text)
