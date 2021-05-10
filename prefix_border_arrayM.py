# Построение модифицированного массива
from prefix_border_array import prefix_border_array


def prefix_border_arrayM(S, bp):
    n = len(S)
    bpm = [0] * n
    bpm[n - 1] = bp[n - 1]
    for i in range(1, n - 1):  # Проверка совпадения следующих символов
        if bp[i] != 0 and S[bp[i]] == S[i + 1]:
            bpm[i] = bpm[bp[i] - 1]
        else:
            bpm[i] = bp[i]

    return bpm


if __name__ == '__main__':
    examples = ['CACZZZCACA', 'ABXABZMABXABZ']
    for i in range(len(examples)):
        example = examples[i]
        print(f'Пример {i + 1}')
        bp = prefix_border_array(example)
        print(f'bp : {bp}')
        print(f'bpm: {prefix_border_arrayM(example, bp)}')
