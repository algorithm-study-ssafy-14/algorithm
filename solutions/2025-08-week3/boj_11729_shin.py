N = int(input())
def dp(num):
    if num == 1:
        return 1
    else:
        return dp(num-1)*2 + 1

def dp_2(num):
    if num == 1:
        return [[1,3]]

    else:
        if memo[num] != 0:
            return memo[num]

        if num % 2 == 0:
            a_list = [0] * dp(num)
            for i in range(len(a_list)):
                if i % 6 == 0:
                    a_list[i] = [1,2]
                elif i % 6 == 2:
                    a_list[i] = [2,3]
                elif i % 6 == 4:
                    a_list[i] = [3,1]
                else:
                    a_list[i] = dp_2(num-1)[i//2]

        else:
            a_list = [0] * dp(num)
            for i in range(len(a_list)):
                if i % 6 == 0:
                    a_list[i] = [1,3]
                elif i % 6 == 2:
                    a_list[i] = [3,2]
                elif i % 6 == 4:
                    a_list[i] = [2,1]
                else:
                    a_list[i] = dp_2(num-1)[i//2]

        memo[num] = a_list
        return a_list

memo = [0]*21

print(dp(N))
result = dp_2(N)

for i in result:
    print(*i)