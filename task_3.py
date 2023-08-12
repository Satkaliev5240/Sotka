def func():
    arr_number = []
    arr_index = []
    for i in range(100,999):
        for j in range(100,999):
            if str(i*j)[::-1] == str(i*j):
                arr_number.append(i*j)
                arr_index.append([i,j])
    return max(arr_number), arr_index[arr_number.index(max(arr_number))]
print(func())