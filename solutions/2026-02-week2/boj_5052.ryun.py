# 전화번호 목록

t = int(input())

for _ in range(t):
    n = int(input())
    numbers = []
    for i in range(n):
        numbers.append(input())

    numbers.sort()
    for i in range(len(numbers)-1):
        if numbers[i+1].startswith(numbers[i]):
            print("NO")
            break
    else:
        print("YES")