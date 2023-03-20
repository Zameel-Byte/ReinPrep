def is_path_found(matrix, x, y):
    stack = [(0, 0)]
    visited = set()

    while stack:
        curr_x, curr_y = stack.pop()
        if (curr_x, curr_y) in visited:
            continue

        if curr_x == x and curr_y == y:
            return True

        visited.add((curr_x, curr_y))

        if curr_x > 0 and matrix[curr_x-1][curr_y] == '1':
            stack.append((curr_x-1, curr_y))
        if curr_y > 0 and matrix[curr_x][curr_y-1] == '1':
            stack.append((curr_x, curr_y-1))
        if curr_x < len(matrix)-1 and matrix[curr_x+1][curr_y] == '1':
            stack.append((curr_x+1, curr_y))
        if curr_y < len(matrix[0])-1 and matrix[curr_x][curr_y+1] == '1':
            stack.append((curr_x, curr_y+1))

    return False


mat = [['1', '0', '1', '1', '0'],
       ['1', '1', '1', '1', '0'],
       ['0', '1', '1', '1', '1'],
       ['0', '0', '0', '1', '1']
       ]
if is_path_found(mat, 3, 4):
    print("Path Found")
else:
    print("Path Not Found")
