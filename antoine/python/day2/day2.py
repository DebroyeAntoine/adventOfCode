import re

rule = {'red': 12, 'blue': 14, 'green': 13}

def parse_file(file, Max=False):
    result = []
    for line in file:
        count_red = 0
        count_blue = 0
        count_green = 0
        substrings = line.split(';')
        for substring in substrings:
            for color in rule:
                match = re.search(r'\b(\d+)\s' + re.escape(color), substring)
                if match:
                    count = int(match.group(1))
                    if color == 'red':
                        if Max:
                            if count > count_red:
                                count_red = count
                        else:
                            count_red = count

                    elif color == 'blue':
                        if Max:
                            if count > count_blue:
                                count_blue = count
                        else:
                            count_blue = count
                    else:
                        if Max:
                            if count > count_green:
                                count_green = count
                        else:
                            count_green = count
            if (count_red > rule['red'] or count_blue > rule['blue'] or count_green > rule['green']) and not Max:
                break
        if (count_red <= rule['red'] and count_blue <= rule['blue'] and count_green <= rule['green']) and not Max:
            result.append(line)
        if Max:
            result.append([count_red, count_blue, count_green])
    return result


def sum_games(games):
    sum = 0
    for game in games:
        match = re.match(r'Game (\d+)', game)
        if match:
            sum += int(match.group(1))
    print(sum)


def find_max(file):
    result = 0
    max_lines = parse_file(file, Max=True)
    for line in max_lines:
        intermediate = 1
        for part in line:
            intermediate = intermediate * part
        result += intermediate
    print(result)



with open("day2.txt", 'r') as filename:
    tmp1 = list(filename)
    tmp2 = tmp1[:]
    parsed_file = parse_file(tmp2)
    sum_games(parsed_file)
    find_max(tmp1)
