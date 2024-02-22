def сircular_array(n: int, m: int):

    array = list(range(1, n + 1))
    path = []

    item = 1
    while True:
        path.append(str(item))
        item = 1 + (item + m - 2) % n
        if item == array[0]:
            break

    print('Resulting path:',''.join(path))


if __name__ == "__main__":
    nums = input().split()
    n, m = int(nums[0]), int(nums[1])
    сircular_array(n, m)