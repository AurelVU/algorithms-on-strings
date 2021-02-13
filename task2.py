def solver(input_string):
    max_gran = 0
    for len_of_gran in range(1, len(input_string)):
        current_count = 0
        while current_count < len_of_gran and input_string[current_count] == input_string[len(input_string) - len_of_gran + current_count]:
            current_count += 1
        if current_count == len_of_gran:
            max_gran = len_of_gran
    return max_gran



input_string = 'test_fdfshjdfs_testh_testf_testdh_testf_testkgfdhdfkg_test_jgfkdfl_test'
print('Максимальная длина грани: ', solver(input_string))

input_string = 'test'
print('Максимальная длина грани: ', solver(input_string))

input_string = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
print('Максимальная длина грани: ', solver(input_string))