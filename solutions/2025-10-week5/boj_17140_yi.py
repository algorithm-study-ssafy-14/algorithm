def new_row(row):
    counts = {}

    for num in row:
        if num == 0:
            continue
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1

    pairs = []

    for key in counts:
        pairs.append([key, counts[key]])

    pairs.sort(key=lambda x: (x[1], x[0]))
    new_row = []

    for a, b in pairs:
        new_row.append(a)
        new_row.append(b)

    if len(new_row) > 100:
        new_row = new_row[:100]
    return new_row

def r_operation(arr):
    new_arr = []
    max_length = 0

    for row in arr:
        new_row = new_row(row)
        new_arr.append(new_row)

        if len(new_row) > max_length:
            max_length = len(new_row)

    for row in new_arr:
        while len(row) < max_length:
            row.append(0)
    return new_arr

def c_operation(arr):
    transposed = []

    for x in range(len(arr[0])):
        new_row = []

        for y in range(len(arr)):
            new_row.append(arr[y][x])
        transposed.append(new_row)

    transposed = r_operation(transposed)
    result = []

    for x in range(len(transposed[0])):
        new_row = []

        for y in range(len(transposed)):
            new_row.append(transposed[y][x])
        result.append(new_row)
    return result


r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]
time = 0

while True:
    if 0 <= r - 1 < len(A) and 0 <= c - 1 < len(A[0]) and A[r - 1][c - 1] == k:
        print(time)
        break
    if time > 100:
        print(-1)
        break
    if len(A) >= len(A[0]):
        A = r_operation(A)
    else:
        A = c_operation(A)
    time += 1

