def prefix_border_array(S):
    n = len(S)
    bp = [0]
    for i in range(1, n):  # i –длина рассматриваемого префикса
        bpRight = bp[i - 1]  # Позиция справа от предыдущей грани
        while bpRight != 0 and S[i] != S[bpRight]:
            bpRight = bp[bpRight - 1]
            # Длина на 1 больше, чем позиция
        if S[i] == S[bpRight]:
            bp.append(bpRight + 1)
        else:
            bp.append(0)
    return bp


if __name__ == '__main__':
    example = 'ABAAABAСBСAABAAAB'
    print(prefix_border_array(example))
