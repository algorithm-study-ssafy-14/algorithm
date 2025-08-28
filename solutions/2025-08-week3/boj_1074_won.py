def z(p_value, p_r, p_c, n):
    value = p_value
    new_n = n // 2

    if n == 2:
        print(value + p_r*2 + p_c)
        return
    else:
        if p_r < new_n:
            if p_c < new_n:
                pass
            else:
                value += new_n**2
        else:
            if p_c < new_n:
                value += new_n**2*2
            else:
                value += new_n**2*3

        z(value, p_r % new_n, p_c % new_n, new_n)
        return


N, r, c = map(int, input().split())

z(0, r, c, 2**N)
