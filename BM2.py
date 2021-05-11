from BM import position_list, badChar_shift
from BS_and_BSM import BS_to_BSM
from suffix_border_array import suffix_border_array


def BS_to_NS(bs, m):
    ns = [0] * m
    for k in range(0, m):
        ns[k] = -1  # Фиктивное значение
        for j in range(0, m - 1):
            # Порядок просмотра bs гарантирует сохранение
            if bs[j] != 0:  # позиций самых правых копий суффиксов
                k = m - bs[j] - 1
                ns[k] = j
    return ns


def BS_to_BR(bs, m):
    br = [0] * m
    currBorder = bs[0]
    k = 0
    while currBorder != 0:
        # k < m - currBorder <=> currBorder < m - k
        while k < m - currBorder:
            br[k] = currBorder
            k += 1
        currBorder = bs[k]  # Меньшая грань образца (k = m - currBorder)
        # - грань грани
    while k < m:
        br[k] = 0
        k += 1

    return br


def goodSuffix_shift(nsx, br, PosBad, m):
    if PosBad == m - 1:
        return 1  # Хорошего суффикса нет
    if PosBad < 0:
        return m - br[0]  # Образец совпал – сдвиг по наиб. грани
    CopyPos = nsx[PosBad]  # Вхождение левой копии суффикса
    if (CopyPos >= 0):
        Shift = PosBad - CopyPos + 1
    else:
        Shift = m - br[PosBad]  # Cдвиг по ограниченной наибольшей грани
    return Shift


def BM(pattern, text, h):  # h = 1 ~ сильное правило хорошего суффикса
    alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]  # Формирование алфавита
    pl = position_list(pattern, alphabet)  # Для правила плохого символа
    m = len(pattern)
    n = len(text)
    bs = suffix_border_array(pattern)
    br = BS_to_BR(bs, m)
    if h != 0:
        bs = BS_to_BSM(bs, m)
    nsx = BS_to_NS(bs, m)
    nTextR = m  # Правая граница «прикладывания» образца

    while nTextR <= n:  # Поиск вхождений
        # Сравнение образца с текстом справа налево
        k = m - 1
        i = nTextR - 1
        while pattern[k] == text[i] and k >= 0:
            k -= 1
            i -= 1
        # Результаты сравнения
        if k < 0:
            print(f"Вхождение с позиции {i + 1}")
        # Продвижение по наиболее эффективному правилу
        nShift = max(badChar_shift(pl, alphabet, text[i], k), goodSuffix_shift(nsx, br, k, m))
        nTextR += nShift


if __name__ == '__main__':
    s1 = 'ABCBCBCCDBABDFSB'
    s2 = 'BCBC'
    BM(s2, s1, 1)
