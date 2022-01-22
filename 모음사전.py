from itertools import product
def solution(word):
    list1 = ['A','E','I','O','U']
    list2 = list(map(list, product('AEIOU',repeat=2)))
    print(list2)
    list3 = list(map(list, product('AEIOU',repeat=3)))
    print(list3)
    list4 = list(map(list, product('AEIOU',repeat=4)))
    list5 = list(map(list, product('AEIOU',repeat=5)))
    data_list = list1 + list2 + list3 + list4 + list5
    for i in range(len(data_list)):
        data_list[i] = ''.join(data_list[i])
    data_list.sort()
    return data_list.index(word)+1
solution("AAAAE")
