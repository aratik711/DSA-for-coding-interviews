"""

In this lesson, we will be considering how to solve the problem of implementing a function that converts a spreadsheet column ID (i.e., “A”, “B”, “C”, …, “Z”, “AA”, etc.) to the corresponding integer. For example, “A” equals 1 because it represents the first column, while “AA” equals 27 because it represents the 27th column.


"""
def spreadsheet_encode_column(str):
    num = 0
    count = len(str) - 1
    for s in str:
        num += 26**count * (ord(s) - ord('A') + 1)
        count -= 1
    return num

print(spreadsheet_encode_column("ZZ"))
