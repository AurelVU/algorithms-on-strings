from BP_and_BPM import BP_to_BPM
from prefix_border_array import prefix_border_array


def KMP(pattern, text):
    bpm = prefix_border_array(pattern)  # Построение массива граней
    m = len(pattern)
    n = len(text)
    bpm = BP_to_BPM(bpm, m)  # Модифицированный массив граней
    k = 0  # Текущий индекс в образце
    # Цикл по символам текста T
    for i in range(n):  # Быстрые продвижения при фиксированном i
        while k != 0 and pattern[k] != text[i]:
            k = bpm[k - 1]
        # «Честное» сравнение очередной пары символов
        if pattern[k] == text[i]:
            k += 1
        if k == m:
            print(f"Вхождение с позиции {i - k + 1}\n")
            k = bpm[k - 1]


if __name__ == '__main__':
    text = 'abcabeabcabcabd'
    pattern = 'abcabd'
    KMP(pattern, text)
