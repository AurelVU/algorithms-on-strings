from suffix_border_array import suffix_border_array


def BS_to_BSM(bs, n):
    bsm = [0] * n
    bsm[n - 1] = 0
    bsm[0] = bs[0]
    for i in reversed(range(1, n - 1)):  # Проверка «совпадения предыдущих символов»
        if bs[i] != 0 and bs[i] + 1 == bs[i - 1]:
            bsm[i] = bsm[n - bs[i]]
        else:
            bsm[i] = bs[i]
    return bsm


def BSM_to_BS(bsm, n):
    bs = [0] * n
    bs[0] = bsm[0]
    bs[n - 1] = 0
    for i in range(1, n - 1):
        bs[i] = max(bs[i - 1] - 1, bsm[i])
    return bs


if __name__ == '__main__':
    examples = ['CACZZZCACA', 'ABXABZMABXABZ']
    for i in range(len(examples)):
        example = examples[i]
        print(f'Пример {i + 1}')
        bs = suffix_border_array(example)
        print(f'bs : {bs}')
        bsm = BS_to_BSM(bs, len(example))
        print(f'bsm: {bsm}')
        print(f'bs = {BSM_to_BS(bsm, len(example))}')
