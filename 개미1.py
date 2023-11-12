w,h=map(int,input().split())
p,q=map(int,input().split())
t=int(input())
cx=(w-p)
cy=(h-q)
dx=1
dy=1
a=p
b=q
s=0
while t:
    if a==p and b==q:
        break
    c=min(cx,cy,t)
    p+=c*dx
    q+=c*dy
    t-=c
    s+=c
    if p==w:
        dx=-1
        cx=p
    elif p==0:
        dx=1
    if q==h:
        dy=-1
        cy=q
    elif q==0:
        dy=-1
    if dx==1:
        cx=w-p
    elif dx==-1:
        cx=p
    if dy==1:
        cy=h-q
    elif dy==-1:
        cy=q
print(s)
print(p,q)

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

move_x = [i for i in range(w)] + [i for i in range(w, 0, -1)]
move_y = [i for i in range(h)] + [i for i in range(h, 0, -1)]

# 개미의 움직임은 반복이므로 시작지점 + 개미가 움직일 시간을 move_x의 길이(2*w)로 나눈 나머지의 길이만 이동하면 된다.
f_x = move_x[(p + t) % (2 * w)]
f_y = move_y[(q + t) % (2 * h)]

print('{} {}'.format(f_x, f_y))