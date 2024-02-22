def min_moves(filepath):
  
    with open(filepath, 'r') as file:
        nums = [int(x) for x in file]

    average = round(sum(nums) / len(nums))

    moves = 0
    for num in nums:
        moves += abs(num - average)

    print(moves)


if __name__ == "__main__":
    min_moves(filepath = 'task4\\numbers.txt')