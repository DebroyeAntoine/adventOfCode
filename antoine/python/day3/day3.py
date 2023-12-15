tmp = ['#', '+', '$', '*']

def check_is_valid(file, line, start, end, len_file, len_line):
    for i in range(max(0, line - 1), line + 2):
        if i == len_file:
            break
        for j in range(max(0, start - 1), end +2):
            if j == len_line:
                break
            if not(file[i][j].isdigit() or file[i][j].isalpha() or file[i][j].isspace() or file[i][j] == '.') :
                return True
    return False


def sum_numbers(file):
    result = 0
    for line in range(len(file)):
        start = None
        for char in range(len(file[line])):
            if (file[line][char]).isdigit() and start is None:
                start = char
            if start is not None and not file[line][char].isdigit():
                end = char - 1
                valid = check_is_valid(file, line, start, end, len(file), len(file[line]))
                if valid:
                    result += int(file[line][start:end+1])
                start = None
    print(result)


with open("day3.txt", 'r') as filename:
    sum_numbers(list(filename))
