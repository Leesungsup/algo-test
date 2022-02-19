def solution(play_time, adv_time, logs):
    answer = ''
    log=[]
    #c="99:59:59"
    c=play_time.split(':')
    play_time=(int(c[0])*3600+int(c[1])*60+int(c[2]))
    all_time=[0 for i in range(play_time+1)]
    k=adv_time.split(':')
    adv_time=(int(k[0])*3600+int(k[1])*60+int(k[2]))
    print(play_time)
    for i in logs:
        s,t=i.split('-')
        print(s,t)
        s=s.split(':')
        t=t.split(':')
        start=(int(s[0])*3600+int(s[1])*60+int(s[2]))
        end=(int(t[0])*3600+int(t[1])*60+int(t[2]))
        all_time[start]+=1
        all_time[end]-=1
    print(log)
    for i in range(1,len(all_time)):
        all_time[i]=all_time[i]+all_time[i-1]
    for i in range(1,len(all_time)):
        all_time[i]=all_time[i]+all_time[i-1]
    most_view = 0                           # 5
    max_time = 0
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < all_time[i] - all_time[i - adv_time]:
                most_view = all_time[i] - all_time[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if most_view < all_time[i]:
                most_view = all_time[i]
                max_time = i - adv_time + 1
    h = max_time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    max_time = max_time % 3600
    m = max_time // 60
    m = '0' + str(m) if m < 10 else str(m)
    max_time = max_time % 60
    s = '0' + str(max_time) if max_time < 10 else str(max_time)
    print(h + ':' + m + ':' + s)
    return h + ':' + m + ':' + s