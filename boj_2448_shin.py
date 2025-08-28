import sys
print = sys.stdout.write

def dp(length,start_r, start_c):
    if length == 3:
        matrix[start_r+1][start_c] = ord(' ')

    else:
        length //= 2
        for r in range(start_r + length, start_r + 2*length):
            for c in range(start_c - (2*length-(r-start_r)-1), start_c + (2*length-(r-start_r))):
                matrix[r][c] = ord(' ')

        dp(length, start_r, start_c)
        dp(length, start_r + length, start_c - length)
        dp(length, start_r + length, start_c + length)

N = int(input())
matrix = []
for i in range(N):
    matrix.append(bytearray(b' '*(N-1-i) + b'*'*(2*i+1) + b' '*(N-1-i)))

dp(N,0,N-1)


#trimmed = '\n'.join(''.join(i) for i in matrix)

for r in matrix:
    print(r.decode()+'\n')