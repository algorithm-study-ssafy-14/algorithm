import sys
input = sys.stdin.readline


    # k  ** i (i는 0부터 지속적으로 증가) 값을 지속적으로 빼내면서
    #트리의 몇번째 줄에 있는지 확인

def location(num):

    i = 0
    while True:
        if num - (K ** i) < 0:
            result = []
            for _ in range(i + 1):
                result.append(num % K)
                num //= K
            break
        else:
            num -= (K ** i)
            i += 1

    #거꾸로 해주고 나중에 같은 부모를 언제 맞났는지 판별
    #for문 인덱스를 뒤에서 접근하는 방법도 있다고 생각하지만, 조금 불편했음.
    result.reverse()

    return result


N, K, Q = map(int, input().split())

# 1진트리일 경우 분리해서 따로

if K == 1:
    for _ in range(Q):
        a, b = map(int, input().split())
        print(abs(a-b))

# 2 이상일시
else:
    #0부터 인덱스를 맞추고 싶었기 때문에 -1씩 뺴줌. (배수 판별시에 유리)
    for _ in range(Q):
        a, b = map(int, input().split())
        a -= 1; b -= 1
        #값이 두 개. 하나씩 line_a, line_b
        #함수 시작
        line_a = location(a)
        line_b = location(b)

        #결과값 출력, 같은 트리의 노드를 만날 때 까지 검색하고, 만났을 떄 break
    
        for i in range(min(len(line_a),len(line_b))):
            if line_a[i] != line_b[i]:
                print(len(line_a) + len(line_b) - 2*i)
                break

        #만나지 않았다면 알맞게 조정
        else:
            print(len(line_a) + len(line_b) - 2 * i - 2)