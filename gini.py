b1 = 1
b2 = 4
s1 = 2
s2 = 3

gini1 = 0
gini2 = 0

if b1+b2 != 0:
    gini1 = 1 - (b1/(b1+b2))*(b1/(b1+b2)) - (b2/(b1+b2))*(b2/(b1+b2))
if s1+s2 != 0:
    gini2 = 1 - (s1/(s1+s2))*(s1/(s1+s2)) - (s2/(s1+s2))*(s2/(s1+s2))

print(gini1)
print(gini2)

w = s1+s2+b1+b2

gini3 = ((b1+b2)/w)*gini1 + ((s1+s2)/w)*gini2

print(gini3)

#Calculate the gini index and save it.
def gini():
    for j in range(len(split_position)):
        if record_count1[j]['Yes']==0 and record_count1[j]['No']==0:
            result1.append(0)
        else:
            result1.append(1-math.pow((record_count1[j]['Yes']/(record_count1[j]['Yes']+record_count1[j]['No'])),2)-math.pow((record_count1[j]['No']/(record_count1[j]['Yes']+record_count1[j]['No'])),2))
        if record_count2[j]['Yes']==0 and record_count2[j]['No']==0:
            result2.append(0)
        else:
            result2.append(1-math.pow((record_count2[j]['Yes']/(record_count2[j]['Yes']+record_count2[j]['No'])),2)-math.pow((record_count2[j]['No']/(record_count2[j]['Yes']+record_count2[j]['No'])),2))
    for j in range(len(split_position)):
        gi.append(round(result1[j]*((record_count1[j]['Yes']+record_count1[j]['No'])/(record_count1[j]['Yes']+record_count1[j]['No']+record_count2[j]['Yes']+record_count2[j]['No']))+result2[j]*((record_count2[j]['Yes']+record_count2[j]['No'])/(record_count1[j]['Yes']+record_count1[j]['No']+record_count2[j]['Yes']+record_count2[j]['No'])),3))