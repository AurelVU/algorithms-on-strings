# Построение модифицированного массива
from prefix_border_array import prefix_border_array


def BP_to_BPM(bp, n):
    bpm = [0] * n
    bpm[n - 1] = bp[n - 1]
    for i in range(1, n - 1):  # Проверка совпадения следующих символов
        if bp[i] != 0 and bp[i] + 1 == bp[i + 1]:
            bpm[i] = bpm[bp[i] - 1]
        else:
            bpm[i] = bp[i]

    return bpm


def BPM_to_BP(bpm, n):
    bp = [0] * n
    bp[n - 1] = bpm[n - 1]
    bp[0] = 0
    for i in reversed(range(1, n - 1)):
        bp[i] = max(bp[i + 1] - 1, bpm[i])
    return bp


if __name__ == '__main__':
    examples = ['CACZZZCACA', 'ABXABZMABXABZ']
    for i in range(len(examples)):
        example = examples[i]
        print(f'Пример {i + 1}')
        bp = prefix_border_array(example)
        print(f'bp : {bp}')
        bpm = BP_to_BPM(bp, len(example))
        print(f'bpm: {bpm}')
        print(f'bp = {BPM_to_BP(bpm, len(example))}')
