def solver(input_string):
    max_gran = 0
    for len_of_gran in range(1, len(input_string)):
        current_char = 0
        while current_char < len_of_gran:
            if input_string[current_char] == input_string[len(input_string) - len_of_gran + current_char]:
                current_char += 1
            elif current_char != len_of_gran:
                max_gran = len_of_gran
    return max_gran



input_string = 'testfdfshjdfs_testh_testf_testdh_testf_testkgfdhdfkg_test_jgfkdfltest'
print('Максимальная длина грани: ', solver(input_string))

input_string = 'test'
print('Максимальная длина грани: ', solver(input_string))
