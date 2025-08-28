def dp(level,r,c,count):
    if level == 1:
        if r == 0:
            if c == 0:
                return count
            else:
                return count+1
        else:
            if c == 0:
                return count+2
            else:
                return count+3

    else:
        level -= 1

        if r < (1<<level) and c < (1<<level):
            result = dp(level, r, c, count)
            return result
        elif r < (1 << level) and c >= (1 << level):
            result = dp(level, r, c - (1 << level), count + ((1<<level))**2)
            return result

        elif r >= (1<<level) and c < (1<<level):
            result = dp(level, r - (1 << level), c, count + 2 * ((1<<level))**2)
            return result

        else:
            result = dp(level, r - (1 << level), c - (1 << level), count + 3 * ((1<<level))**2)
            return result
# ==============================================================================================
N, r, c = map(int, input().split())
result = dp(N,r,c,0)
print(result)