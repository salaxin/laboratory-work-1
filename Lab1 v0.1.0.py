while True:
    try:
        state = int(input("Выбери номер задачи(1 или 2) или отрицательное число для выхода:"))
    except ValueError:
        print("Это не число")
    if state == 1:
        print("Первое задание")
    elif state == 2:
        print("Второе задание")
    elif state < 0:
        break
    else:
        print("Число находится вне диапазона")
