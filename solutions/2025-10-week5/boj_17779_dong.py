N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
 
result = []
for i in range(N):
    for j in range(N):
        for d1 in range(1, min(j, N-i-1)+1):
            for d2 in range(1, min(N-j-1, N-i-1)+1):
                if i + d1 + d2 <= N-1:
                    value1 = 0
                    value2 = 0
                    value3 = 0
                    value4 = 0
                    value5 = 0
                  
                    for a in range(N):
                        for b in range(N):
                            if i+j <= a+b <= i+j+2*d2 and i-j <= a-b <= i-j+2*d1:
                                value5 += arr[a][b]
                            elif 0 <= a < i+d1 and 0 <= b <= j and a+b < i+j:
                                value1 += arr[a][b]
                            elif 0 <= a <= i+d2 and j < b <= N-1 and a-b < i-j:
                                value2 += arr[a][b]
                            elif i+d1 <= a <= N-1 and 0 <= b < j - d1 + d2 and a-b > i-j+2*d1:
                                value3 += arr[a][b]
                            elif i+d2 < a <= N-1 and j-d1+d2 <= b <= N-1 and a+b > i+j+2*d2:
                                value4 += arr[a][b]
                              
                    result.append(max(value1, value2, value3, value4, value5) - min(value1, value2, value3, value4, value5))
 
print(min(result))