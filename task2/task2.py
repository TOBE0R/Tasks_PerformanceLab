def check_dots(circle_path: str, dot_path: str):
    with open(circle_path, 'r') as input_file:
        center = tuple(map(float, input_file.readline().split()))
        radius = float(input_file.readline())

    with open(dot_path, 'r') as input_file:
        dots = [tuple(map(float, line.split())) for line in input_file]

    for x, y in dots:
        dx = x - center[0]
        dy = y - center[1]
        dist = (dx**2 + dy**2)**0.5
    
        if dist == radius :
            print(0)
        elif dist < radius:  
            print(1)
        else:
            print(2)


if __name__ == "__main__":
    check_dots(circle_path = 'task2\\circle.txt', dot_path = 'task2\\dot.txt')