def shift_and_fz(P, T, k):
    m = len(P)
    n = len(T)
    # Алфавит: например, от цифр до букв латиницы
    # chBeg = '0'
    # chEnd = 'z'
    # nA = ord(chEnd) - ord(chBeg) + 1  # Длина алфавита
    # # Подготовка массива вхождений символов алфавита
    # B = [0] * nA

    B = {}
    for i in range(ord('A'), ord('Z') + 1):
        B[chr(i)] = 0
    for i in range(ord('0'), ord('9') + 1):
        B[chr(i)] = 0
    for j in range(m):
        B[P[j]] |= 1 << (m - 1 - j)

    for j in range(m):
        B[P[j]] |= 1 << (m - j - 1)
    uHigh = 1 << (m - 1)  # Константа для установки 1 в старший разряд
    # Инициализация строк (M1 можно заменить парой переменных)

    M = [0] * (k + 1)
    M1 = [0] * (k + 1)

    for i in range(n):
        # Вычисление «строк матриц» и фиксация вхождений
        for l in range(k + 1):
            M1[l] = M[l]  # Запомнить (i-1)-ю строку
            M[l] = (M[l] >> 1 | uHigh) & B[T[i]]
            if l != 0:
                M[l] |= (M1[l - 1] >> 1 | uHigh)  # Используем (i-1)-ю строку
            if l == k and M[l] & 1:
                # Найдено вхождение
                print(f"Вхождение с позиции {i - m + 1}")


if __name__ == '__main__':
    s1 = 'ABCBCBCCDBCBDFSB'
    s2 = 'BCBC'
    shift_and_fz(s2, s1, 2)
