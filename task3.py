def str_comp(S, n, i1, i2):
    eq_len = 0
    while i1 < n and i2 < n and S[i1] == S[i2]:
        i1 += 1
        i2 += 1
        eq_len += 1
    return eq_len


def prefix_Z_values(S):
    n = len(S)
    l = 0
    r = 0
    zp = [0]
    for i in range(1, n):
        zp.append(0)
        if i >= r:
            zp[i] = str_comp(S, n, 0, i)
            l = i
            r = l + zp[i]
        else:
            j = i - l
            if zp[j] < r - i:
                zp[i] = zp[j]
            else:
                zp[i] = r - i + str_comp(S, n, r - i, r)
                l = i
                r = l + zp[i]
    return zp


test_str = 'AABCAABXAAZ'

print(test_str)
result = prefix_Z_values(test_str)
for i in range(len(result)):
    print(f'Z{i} = {result[i]}')
