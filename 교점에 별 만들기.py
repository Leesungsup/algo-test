from collections import combinations
def interation(line1,line2):
    a,b,e=line1
    c,d,f=line2
    if a*d==b*c:
        return False
    x=(b*f-e*d)/(a*d-b*c)
    y=(e*c-a*f)/(a*d-b*c)
    if x==int(x) and int(y):
        return (int(x),int(y))
def solution(line):
    answer = []
    n=len(line)
    combs=list(combinations(line,2))
    points=set()
    for i in combs:
        point=interation(i[0],i[1])
        if point:
            points.add(point)
    xs=[p[0] for p in points]
    x_min = min(xs)
    x_max = max(xs)
    ys=[p[1] for p in points]
    y_min=min(ys)
    y_max=max(ys)
    answer=['.'*(x_max-x_min)]*(y_max-y_min)
    for point in points:
        x,y = point
        answer[y_max-y] = answer[y_max-y][:x-x_min] + '*' + answer[y_max-y][x-x_min+1:]
    return [''.join(ans) for ans in answer]
