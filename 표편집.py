def solution(n, k, cmd):
    answer = ''
    arr=[i for i in range(n)]
    arr1=['X' for i in range(n)]
    #print(arr1[7])
    cur=k
    d=[]
    for i in cmd:
        #print(i)
        if i[0]=='D':
            dire,number=i.split()
            #print(dire,number)
            cur+=int(number)
        elif i[0]=='U':
            dire,number=i.split()
            #print(dire,number)
            cur-=int(number)
        elif i[0]=='C':
            if cur!=len(arr)-1:
                d.append(int(arr[cur]))
                del arr[cur]
            else:
                d.append(int(arr[cur]))
                del arr[cur]
                cur-=1
        elif i[0]=='Z':
            cn=d.pop(-1)
            arr.insert(cn,cn)
            if cur>cn:
                cur+=1
        #print(d)
        #print(cur,arr[cur])
        #print(arr)
    #print(arr)
    for i in arr:
        #print(i,arr1[i])
        if arr1[i]=='X':
            arr1[i]='O'
    #print(arr1)
    return ''.join(arr1)
def solution1(n, k, cmd):
    answer = ''

    linked_list = {i: [i - 1, i + 1] for i in range(1, n+1)}
    OX = ["O" for i in range(1,n+1)]
    stack = []
    print(linked_list)
    k += 1

    for c in cmd:
        if c[0] == 'D':
            for _ in range(int(c[2:])):
                k = linked_list[k][1]
        elif c[0] == 'U':
            for _ in range(int(c[2:])):
                k = linked_list[k][0]
        elif c[0] == 'C':
            prev, next = linked_list[k]
            stack.append([prev, next, k])
            OX[k-1] = "X"
            if next == n+1:
                k = linked_list[k][0]
            else:
                k = linked_list[k][1]

            if prev == 0:
                linked_list[next][0] = prev
            elif next == n+1:
                linked_list[prev][1] = next
            else:
                linked_list[prev][1] = next
                linked_list[next][0] = prev

        elif c[0] == 'Z':
            prev, next, now = stack.pop()
            OX[now-1] = "O"

            if prev == 0:
                linked_list[next][0] = now
            elif next == n+1:
                linked_list[prev][1] = now
            else:
                linked_list[prev][1] = now
                linked_list[next][0] = now

    return "".join(OX)
solution1(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
