def shift_and(P, T):
    m = len(P)
    n = len(T)
    chBeg = '0'
    chEnd = 'z'  # Алфавит: от цифр до букв латиницы
    nA = ord(chEnd) - ord(chBeg) + 1  # Длина алфавита
    # Подготовка массива вхождений
    B = [0] * nA
    for j in range(m):
        B[P[j] - chBeg] |= 1 << (m - 1 - j)
    uHigh = 1 << (m - 1)  # Константа для установки 1 в старший разряд
    M = 0
    # Вычисление «строк матрицы» и фиксация вхождений
    for i in range(n):
        M = (M >> 1 | uHigh) & B[T[i] - chBeg]
        if M & 1:
            print(f"Вхождение с позиции {i - m + 1}\n", )
