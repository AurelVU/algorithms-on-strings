def position_list(S, A):
    nA = len(A)
    m = len(S)
    pl = [None] * nA

    for k in reversed(range(m)):
        ich = ord(S[k]) - ord(A[0])  # Индекс от начального символа алфавита
        if not pl[ich]:
            pl[ich] = []
        pl[ich].append(k)  # Добавить к списку – реализуется типом IntList
    return pl


# Вычисление сдвига по плохому символу
def badChar_shift(pl, alphabet, CharBad, PosBad):
    if PosBad < 0:
        return 1  # Образец совпал – сдвиг на 1
    nPos = -1  # Искомая позиция слева от плохого символа
    List = pl[ord(CharBad) - ord(alphabet[0])]  # Список позиций данного символа CharBad
    if List:  # Список не пуст
        nLen = len(List)  # Длина списка
        # Ищем элемент, меньший чем плохая позиция
        for k in range(nLen):
            if List[k] < PosBad:
                nPos = List[k]
                break

    return PosBad - nPos


# Поиск вхождений – начальная версия БМ
def BM(pattern, text):
    alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]  # Формирование алфавита
    pl = position_list(pattern, alphabet)
    m = len(pattern)
    n = len(text)
    # Поиск вхождений
    nTextR = m  # Правая граница «прикладывания» образца
    i = 0
    k = 0
    while nTextR <= n:
        # Сравнение образца с текстом справа налево
        k = m - 1
        i = nTextR - 1

        while pattern[k] == text[i] and k >= 0:  # text[i] – плохой символ
            k -= 1
            i -= 1

        # Результаты сравнения
        if k < 0:
            print(f"Вхождение с позиции {i + 1}\n")
        # Продвижение по правилу
        nTextR += badChar_shift(pl, alphabet, text[i], k)


s1 = 'ABCBCBCCDBABDFSB'
s2 = 'BCBC'
print(BM(s2, s1))
