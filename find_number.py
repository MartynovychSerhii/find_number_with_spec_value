def find_number_with_spec_value(li):
    array = []
    for i in li:
        for j in str(i):
            if ord(j) == 51:
                array.append(i)
    return array


result = find_number_with_spec_value([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 55, 75, 333, 698, 351, 83, 0, 4, 56, 321])
print(result)

