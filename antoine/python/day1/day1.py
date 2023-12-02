def extract(file):  
    with open(file, 'r') as file_name:
        line_res = []
        for line in file_name:
            numbers = [char for char in line if char.isdigit()]
            line_res.append(int(numbers[0]) * 10 + int(numbers[len(numbers)-1]))
        return line_res

extract_total = extract("day1.txt")
res = 0
for value in extract_total:
    res += value

print(res)
