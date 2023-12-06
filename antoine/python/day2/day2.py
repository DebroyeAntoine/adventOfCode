import re

rule = {'red': 12, 'blue': 14, 'green': 13}

def parse_file(file):
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
                    if color == 'red':
                        count_red = int(match.group(1))
                    elif color == 'blue':
                        count_blue = int(match.group(1))
                    else:
                        count_green = int(match.group(1))
            if count_red > rule['red'] or count_blue > rule['blue'] or count_green > rule['green']:
                break
        if count_red <= rule['red'] and count_blue <= rule['blue'] and count_green <= rule['green']:
            result.append(line)
    return result


def sum_games(games):
    sum = 0
    for game in games:
        match = re.match(r'Game (\d+)', game)
        if match:
            print(match.group(1))
            sum += int(match.group(1))
    print(sum)



with open("day2.txt", 'r') as filename:
    parsed_file = parse_file(filename)
    sum_games(parsed_file)
