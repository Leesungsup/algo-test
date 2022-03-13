target = 'ABC'
text = 'ABABCA'

for i in range(len(text)-len(target)):
    for j in range(len(target)):
        if text[i+j] == target[j]:
            j+=1
        else:
            break

    print('Identified')
    break