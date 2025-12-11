def in_order(node):
    if node is None:
        return
    char, left, right = tree[node]
    #왼쪽
    in_order(left)
    #현재
    result.append(char)
    #오른쪽
    in_order(right)

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    tree = {}
    
    for _ in range(N):
        parts = input().split()
        num = int(parts[0])
        char = parts[1]
        # 왼쪽 자식이 있을 경우
        if len(parts) >= 3:
            left = int(parts[2])
        else:
            left = None
        # 오른쪽 자식이 있을 경우
        if len(parts) == 4:
            right = int(parts[3])
        else:
            right = None
        tree[num] = (char, left, right)
    
    result = [] 
    in_order(1)
    print(f"#{test_case} {''.join(result)}")

