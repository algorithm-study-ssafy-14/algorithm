def r_cal(li: list):                                    # row 계산 함수
    max_len = 0
    for i in range(len(li)):
        dict = {}

        for num in li[i]:                               # 행의 원소들을 보고 딕셔너리로 정리
            if num == 0:                                # 0은 무시
                continue
            dict[num] = dict.get(num, 0) + 1

        sub_li = []                                     # 계산 값들을 넣어둘 sub list

        for key, value in sorted(dict.items(), key=lambda x: (x[1], x[0])):     # sorted 는 key 값을 오름차순으로 정렬함. value 값으로 정렬해야해서
            sub_li.append(key)                                                  # 람다를 사용함.
            sub_li.append(value)

        if len(sub_li) > 100:                           # 길이 100 제한
            sub_li = sub_li[:100]

        li[i] = sub_li                                  # li[i] 에 넣어줌.
        if max_len < len(sub_li):
            max_len = len(sub_li)

    for i in range(len(li)):                        # max_len 보다 짧은 행들은 0 으로 채워줌
        if len(li[i]) < max_len:
            li[i].extend([0] * (max_len - len(li[i])))


def c_cal(li: list):
    if not li or not li[0]:
        return
    translate = [list(row) for row in zip(*li)]        # 배열을 돌려서 r_cal 을 사용함.
    r_cal(translate)
    sub_arr = [list(row) for row in zip(*translate)]   # 원상복귀
    li.clear()
    li.extend(sub_arr)


def check_row_col(li: list):                            # row 계산을 할지 col 계산을 할지 정하는 함수
    return len(li) >= len(li[0])


def check_k():
    if 1 <= r <= len(A) and 1 <= c <= len(A[0]):
        return A[r - 1][c - 1] == k
    return False


r, c, k = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(3)]

result = 0
while not check_k() and result <= 100:
    if check_row_col(A):
        r_cal(A)
    else:
        c_cal(A)

    result += 1

print(-1 if result > 100 else result)