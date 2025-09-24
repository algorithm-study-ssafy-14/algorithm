def solution(N, number):
    arr = [set([int(str(N)*(i+1))]) for i in range(8)]
    
    for i in range(8):
        for j in range(i):
            for k in arr[j]:
                for h in arr[i-j-1]:
                    arr[i].add(k+h)
                    arr[i].add(k-h)
                    arr[i].add(h-k)
                    arr[i].add(k*h)
                    if h != 0:
                        arr[i].add(k//h)
                    if k != 0:
                        arr[i].add(h//k)
        if number in arr[i]:
            return i+1
    return -1