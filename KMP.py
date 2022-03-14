def KMP_table(pattern):
    lp=len(pattern)
    tb=[0 for _ in range(lp)]
    pidx=0
    for idx in range(1,lp):
        while pidx>0 and pattern[idx]!=pattern[pidx]:
            print(pidx)
            pidx=tb[pidx-1]
        if pattern[idx]==pattern[pidx]:
            pidx+=1
            tb[idx]=pidx
    return tb
print(KMP_table("ABXCABC"))
def KMP(word,pattern):
    table=KMP_table(pattern)
    results=[]
    pidx=0
    for idx in range(len(word)):
        while pidx>0 and word[idx] != pattern[pidx]:
            pidx=table[pidx-1]
        if word[idx] == pattern[pidx]:
            if pidx == len(pattern)-1 :
                results.append(idx-len(pattern)+2)
                pidx = table[pidx]
            else:
                pidx += 1

    return results
