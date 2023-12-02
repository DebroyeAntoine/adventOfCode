numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def words_to_line(file):
    new_file = []
    for line in file:
        for i, number in enumerate(numbers):
            if number in line:
                # Not the best way to do it for sure.
                # Here I let the first and last letter of the digit to avoid removing one digit
                # like with eightwo wich is 82 and not only 8
                line = line.replace(number, number[0]+str(i+1)+number[len(number)-1])
        new_file.append(line)
    return new_file


def extract(file):
    line_res = []
    for line in file:
        numbers = [char for char in line if char.isdigit()]
        line_res.append(int(numbers[0]) * 10 + int(numbers[len(numbers)-1]))
    return line_res


with open("day1.txt", 'r') as filename:
    file = words_to_line(filename)
    extract_total = extract(file)
    res = 0
    for value in extract_total:
        res += value
    
    print(res)
