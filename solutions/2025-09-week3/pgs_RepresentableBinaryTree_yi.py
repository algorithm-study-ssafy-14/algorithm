def solution(numbers):
    answer = [1] * len(numbers)
    arr = []
    for i in numbers:
        arr.append(bin(i)[2:])
    for i in range(len(arr)):
        length = 1
        while length < len(arr[i]):
            length = length * 2 + 1
        arr[i] = arr[i].zfill(length)
    # print(arr)
    for i in range(len(arr)):
        stack = [arr[i]]
        while stack:
            s = stack.pop()
            if len(s) == 1:
                continue
            mid = len(s) // 2
            root = s[mid]
            left = s[:mid]
            right = s[mid + 1:]
            if root == '0' and ('1' in left or '1' in right):
                answer[i] = 0
                break
            stack.append(left)
            stack.append(right)
    return answer


numbers = [63, 111, 95]
print(solution(numbers))