import sys
n = int(sys.stdin.readline())
char = str(sys.stdin.readline().rstrip())
count=[]
alphabet=[0]*27
for i in char:
    if i not in count:
        count.append(i)
for length in range(1,len(count)+1):
    answer = [0, 0]
    start = 0
    end = 0
    s = {}
    while start < len(char) and end < len(char):
        if char[end] not in s:
            s[char[end]] = 1
        else:
            s[char[end]] += 1
        if len(s) > length:
            print(s)
            while start <= end and len(s) > length:
                if s[char[start]] == 1:
                    s.pop(char[start])
                else:
                    s[char[start]] -= 1
                start += 1
        if len(s) <= length:
            if answer[1] - answer[0] < end - start:
                answer[0] = start
                answer[1] = end
        end += 1
    alphabet[length]=answer[1] - answer[0] + 1
for i in range(1,27):
    print(alphabet[i])