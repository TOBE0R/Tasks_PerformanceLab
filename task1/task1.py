def сircular_array(n: int, m: int):
    
    path = []
    item = 1
    while True:
        path.append(str(item))
        item = 1 + (item + m - 2) % n
        if item == 1:
            break

    print('Resulting path:',''.join(path))


if __name__ == "__main__":
    while True:
        nums = input('Введите n и m через пробел (n, m - натуральные числа): ').split()
        try:
            n, m = int(nums[0]), int(nums[1])
            break
        except:
            print('Некорректный ввод данных, попробуйте снова')
    сircular_array(n, m)