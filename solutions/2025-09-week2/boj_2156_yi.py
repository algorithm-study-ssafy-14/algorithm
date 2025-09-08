n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
dp = [0] * (n + 1)  # dp배열 0으로 초기화
if n == 1:  # 잔 개수가 3개 이하일때 각각 초기화
    ans = arr[0]
elif n == 2:
    ans = arr[0] + arr[1]
elif n == 3:
    ans = max(arr[1] + arr[0], arr[1] + arr[2], arr[0] + arr[2])  # 1개일때는 생각 배제(어차피 최대를 구해야하니까)
else:
    dp[0] = arr[0]
    dp[1] = arr[1] + arr[0]
    dp[2] = max(arr[1] + arr[0], arr[1] + arr[2], arr[0] + arr[2])
    for i in range(3, n):  # 인덱스 3 이상부터 계산 3미만은 경우의 수가 단순하기 때문  
        a = dp[i - 1]  # 인덱스 대상이 안마실때
        b = dp[i - 2] + arr[i]  # 인덱스 대상이 마시고, 그 전 잔은 건너뛰고 전전잔을 마실경우
        c = dp[i - 3] + arr[i] + arr[i - 1]  # 인덱스 대상이 마시고, 그 전 잔을 마셨는데 이 경우 연속 3잔을 피하기 위해 전전잔은 건너뛰는 경우
        dp[i] = max(a, b, c)  # 해서 3가지 경우 중 최대값
    ans = max(dp)
print(ans)