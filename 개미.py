w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
a = (p + t) // w
b = (q + t) // h
if a % 2 == 0 :
    p = (p + t) % w
else :
    p = w - (p + t) % w
if b % 2 == 0 :
    q = (q + t) % h
else :
    q = h - (q + t) % h
print(p, q)

w,h=map(int,input().split())
p,q=map(int,input().split())
t=int(input())
dx=1
dy=1
c_x=w-p
c_y=h-q
while t:
    c=min(c_x,c_y,t)
    t-=c
    p+=c*dx
    q+=c*dy
    if p==w:
        dx=-1
        c_x=p
    elif p==0:
        dx=1
    if q==h:
        dy=-1
        c_y=q
    elif q==0:
        dy=1
    if dx==1:
        c_x=w-p
    elif dx==-1:
        c_x=p
    if dy==1:
        c_y=h-q
    elif dy==-1:
        c_y=q
print(p,q)

w,h=map(int,input().split())
p,q=map(int,input().split())
t=int(input())
dx=1
dy=1
for i in range(t):
    if p==w:
        dx=-1
    else:
        dx=1
    if q==h:
        dy=-1
    else:
        dy=-1
    p+=dx
    q+=dy
print(p,q)