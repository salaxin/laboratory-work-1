def merge_arrays(array1, array2):
    merged_array = list(set(array1) & set(array2))
    return merged_array

while True:
    try:
        state = int(input("Выбери номер задачи(1 или 2) или отрицательное число для выхода:"))
    except ValueError:
        print("Это не число")
    if state == 1:
        print("Первое задание")
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [4, 5, 6, 7, 8]
        result = merge_arrays(arr1, arr2)
        print(result)  # [4, 5]
    elif state == 2:
        print("Второе задание")
    elif state < 0:
        break
    else:
        print("Число находится вне диапазона")
