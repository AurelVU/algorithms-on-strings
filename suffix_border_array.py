# Вычисление массива граней суффиксов

def suffix_border_array(S):
    n = len(S)
    bs = [0] * n

    for i in reversed(range(0, n - 1)):
        bsLeft = bs[i + 1]  # Позиция с конца слева от предыдущей грани
        while bsLeft != 0 and S[i] != S[n - bsLeft - 1]:
            bsLeft = bs[n - bsLeft]
        # Длина на 1 больше, чем позиция
        if S[i] == S[n - bsLeft - 1]:
            bs[i] = bsLeft + 1
        else:
            bs[i] = 0

    return bs


if __name__ == '__main__':
    example = 'ABAAABAСBСAABAAAB'
    print(suffix_border_array(example))
