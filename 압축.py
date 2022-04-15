def solution(msg):
    answer = []
    dic = {}
    #사전 제작
    for i in range(26):
        dic[chr(65+i)] = i+1
    w, c = 0, 0
    while True:
        c += 1
        if c == len(msg):
            answer.append(dic[msg[w:c]])
            break
        #남은 문자와 사전을 비교하여 index 출력
        if msg[w:c+1] not in dic:
            dic[msg[w:c+1]] = len(dic) + 1
            answer.append(dic[msg[w:c]])
            w = c
    return answer