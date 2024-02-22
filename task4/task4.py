def min_moves(filepath):
  
    with open(filepath, 'r') as file:
        nums = [int(x) for x in file]
    
    median = sorted(nums)[len(nums) // 2]

    moves = 0
    for num in nums:
        moves += abs(num - median)

    print(moves)


if __name__ == "__main__":
    min_moves(filepath = 'task4\\numbers.txt')