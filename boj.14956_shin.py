def dfs(n, loc):
    global x, y
    if n == 1:
        return
    
    p = (n**2) // 4
    m = n//2
    mini_loc = loc % p

    dfs(m, mini_loc)
    #1사분면
    if loc <  p:
        x, y = y, x


    #2사분면
    elif loc < 2 * p:
        y += m


    #3사분면
    elif loc < 3 * p:
        x += m
        y += m

    #4사분면
    else:
        x, y = m-1-y, m-1-x
        x += m

n, k = map(int, input().split())
k -= 1
x = y = 0
dfs(n, k)
print(x+1,y+1)