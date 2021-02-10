def naive_string_match(input_string, founded_string):
    n = len(input_string)
    m = len(founded_string)
    current_len = n - m + 1
    for i in range(current_len):
        j = 0
        while j < m and founded_string[j] == input_string[i + j]:
            j += 1
        if j == m:
            print("Найдено вхождение в позиции " + str(i))

input_string = 'string Some  stri string for this task string'
founded_string = 'string'

naive_string_match(input_string, founded_string)
