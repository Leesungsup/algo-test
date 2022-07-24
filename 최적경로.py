def dfs(index, lastX, lastY, distance):
    global min_count
    if min_count < distance:
        return
    if index == length:
        distance += abs(lastX - home_position[0]) + abs(lastY - home_position[1])
        min_count = min(distance, min_count)
        return
    for i in range(length):
        if check[i]:
            check[i] = False
            temp = distance + abs(lastX - position_list[i][0]) + abs(lastY - position_list[i][1])
            dfs(index+1, position_list[i][0], position_list[i][1], temp)
            check[i] = True


T = int(input())
for t in range(1, T+1):
    length = int(input())
    temp_list = list(map(int, input().split()))
    position_list = []
    check = [True for _ in range(length)]
    min_count = 1000

    company_position = []
    home_position = []
    for i in range(0, len(temp_list), 2):
        position_list.append([temp_list[i], temp_list[i+1]])
    company_position = position_list.pop(0)
    home_position = position_list.pop(0)
    dfs(0, company_position[0], company_position[1], 0)
    print("#{} {}".format(t, min_count))
