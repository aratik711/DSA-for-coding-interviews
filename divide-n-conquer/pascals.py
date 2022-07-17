"""

The time complexity of this solution is O(linenumber)
, since starting from the first line, we use previous lines to calculate the current line. The loop on Line 25-35 runs at most line_number (where line_number is equal to the max number of rows in the Pascal’s triangle) times at the first call to the function.



"""

def pascal_triangle_recursive(line_number, space):
    current_line_size = line_number
    previous_line_size = current_line_size - 1
    if line_number == 1:
        current_line = [0] * current_line_size
        current_line[0] = 1
        return current_line
    else:
        current_line = [0] * current_line_size
        previous_line = pascal_triangle_recursive(line_number-1, space+1)
        for numIndex in range(current_line_size):
            if (numIndex-1) >= 0:
                left_coeff = previous_line[numIndex-1]
            else:
                left_coeff = 0
            if numIndex < previous_line_size:
                right_coeff = previous_line[numIndex]
            else:
                right_coeff = 0
            current_line[numIndex] = left_coeff + right_coeff
    for i in range(space):
        print(" ", end=" ")
    print(previous_line)
    return current_line



# Driver code to test the above function
if __name__ == '__main__':


    # you can change this
    line_number = 5
    lst = pascal_triangle_recursive(line_number + 1, line_number+1//2)
