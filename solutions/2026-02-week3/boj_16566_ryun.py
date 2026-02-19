## 카드 게임

n, m, k = map(int, input().split())
card_list = list(map(int, input().split()))
attack_order = list(map(int, input().split()))

depth_info = n - 1
depth = 0
while depth_info:
    depth_info //= 2
    depth += 1

added_arr = 2 ** depth

seg_tree = [0] * (added_arr + n)

#세그트리에 입력
for num in card_list:
    altered_num = added_arr + num - 1

    while altered_num:
        seg_tree[altered_num] += 1
        altered_num //= 2

#===================== 여긲지는 맞음
ans_arr = []
# 세그트리에서 더 큰 수 찾아내기
for num in attack_order:

    #일단 대상의 수를 먼저 찾는다
    #이전의 수를 찾으면 안된다 (확인 필요)
    altered_num = added_arr + num - 1 # - 1 + 1 #자신의 다음수부터 있는지 확인

    while True:
        (altered_num, not_valid) = divmod(altered_num, 2)
        if not not_valid and seg_tree[altered_num * 2 + 1]:
            altered_num = altered_num * 2 + 1

            # 우선 끝까지 세그트리 최신화
            temp = altered_num
            while seg_tree[temp]:
                seg_tree[temp] -= 1
                temp //= 2

            break
        #수가 있는 세그트리가 발견되면 바로 내려간다.
    # 내려가자.
    while altered_num < added_arr:
        altered_num *= 2
        if seg_tree[altered_num]:
            seg_tree[altered_num] -= 1

        else:
            altered_num += 1
            seg_tree[altered_num] -= 1


    else:
        if seg_tree[altered_num]:
            seg_tree[altered_num] -= 1
            print(altered_num - added_arr)
        else:
            print(altered_num - added_arr + 1)
