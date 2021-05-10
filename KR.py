def gorner2mod(S, m, q):
    res = 0
    for i in range(m):
        res = (res * 2 + S[i]) % q
    return res


def KR(P, T, q):
    # Инициализация
    m = len(P)
    n = len(T)  # ?
    p2m = 1  # Для вычисления p2m = 2**(m-1) mod q
    for i in range(m - 1):
        p2m = (p2m * 2) % q
    hp = gorner2mod(P, m, q)
    ht = gorner2mod(T, m, q)
    for j in range(n - m + 1):  # Поиск вхождений
        if ht == hp:  # Уточнить, действительно ли совпали строки
            k = 0
            while k < m and P[k] == T[j + k]:
                k += 1
            if k == m:
                print(f"Вхождение с позиции {j}\n")

        ht = ((ht - p2m * T[j]) * 2 + T[j + m]) % q
        if ht < 0:
            ht += q  # Модулярная арифметика
