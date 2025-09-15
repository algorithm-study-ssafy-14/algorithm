def solution(numbers):


    #결과값 받는 변수를 미리 등록
    result_list = []

    # 2의 제곱으로 커지는 값을 계속 뺴면서 height의 높이 정보를 받아옴.
    #예를 들어, 이진수로 표현되었을 때  아잔수의 길이가 4~7이라면 이 트리의 총 높이는 3이 됨.
    for i in numbers:
        num_bin = bin(i)
        height = 0
        while True:
            if len(num_bin)-2 < 2 ** height:
                break

            else:
                height += 1

        #길이가 결정되었다면 이제 뒤에서부터 값을 찾음.
        #꼭 2의 제곱을 다 채우지 않고 앞부분이 0으로 비는 경우가 있기 때문에 미리 리스트의 앞부분을 '0'으로 잡아놓고,
        #뒤부터 이진수를 채워줌.
        num_list = ['0'] * ((2 ** height))
        t = -1
        for i in range(len(num_bin)-1, 1, -1):
            num_list[t] = num_bin[i]
            t -= 1

        #가능한 이진수인지 판별시작.
        #1이면 어떤 경우에도 패스이기 때문에 컨티뉴.
        for i in range(2, len(num_list),2):
            if num_list[i] == '1':
                continue
            
        #0이라면 그 자식에 해당하는 값이 0이어야 하기 때문에 그것에 대한 판별.
            else:
                count = -1
                temp = i
                while True:
                    if temp % 2 == 0:
                        temp //= 2
                        count += 1

                    else:
                        break
                #num_list[i - (2**count)], num_list[i + (2**count)]는 판별대상의 자식을 나타냄.
                #0이 아니라면 0을 result에 입력 후 break로 탈출
                if count >= 0:
                    if num_list[i - (2**count)] == num_list[i + (2**count)] == '0':
                        continue
                    else:
                        result_list.append(0)
                        break
            #모든 수가 정해진 규칙을 만족했을 시 1을 result에 입력 후 탈출
        else:
            result_list.append(1)

    return result_list