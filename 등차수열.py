def find_smallest_x(a, b, c):
    y = (a + c) / 2.0
    x = y - b
    return x
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    a, b, c = map(int, input().split())
    print(a,b,c)
    # 등차수열을 이루도록 하는 가장 작은 x 값을 찾아 출력
    x = find_smallest_x(a, b, c)
    print("#%d %.1f"%(i, x))