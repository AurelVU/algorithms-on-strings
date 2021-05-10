# Алгоритм поиска z-значений

def str_comp(in_string, left_index, right_index):
    eq_len = 0
    n = len(in_string)
    while left_index < n and right_index < n and in_string[left_index] == in_string[right_index]:
        left_index += 1
        right_index += 1
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
            zp[i] = str_comp(S, 0, i)
            l = i
            r = l + zp[i]
        else:
            j = i - l
            if zp[j] < r - i:
                zp[i] = zp[j]
            else:
                zp[i] = r - i + str_comp(S, r - i, r)
                l = i
                r = l + zp[i]
    return zp


if __name__ == '__main__':
    test_str = 'AABCAABXAAZ'

    print(test_str)
    result = prefix_Z_values(test_str)
    for i in range(len(result)):
        print(f'Z{i} = {result[i]}')
