def StrCompBack(S, i1, i2):
    eqLen = 0
    while i1 >= 0 and i2 >= 0 and S[i1] == S[i2]:
        eqLen += 1
        i1 -= 1
        i2 -= 1
    return eqLen


def suffix_Z_values(S):
    n = len(S)
    l = n - 1
    r = n - 1
    zs = [0] * n
    for i in reversed(range(0, n - 1)):
        # zs[i] = 0
        if i <= l:
            # Позиция i не покрыта Z-блоком – он вычисляется заново
            zs[i] = StrCompBack(S, i, n - 1)
            r = i
            l = r - zs[i]
        # Вычисление массива Z-значений суффиксов
        else:  # Позиция i покрыта Z-блоком – он используется
            j = n - (r + 1 - i)
            if (zs[j] < i - l):
                zs[i] = zs[j]
            else:
                zs[i] = i - l + StrCompBack(S, l, n - i + l)
                r = i
                l = r - zs[i]
    return zs


