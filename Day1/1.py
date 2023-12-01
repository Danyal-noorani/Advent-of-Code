def sol1_part1():
    with open("File1") as file:
        data = file.readlines()
        for i in data:
            data[data.index(i)] = [j for j in i if j.isdigit()]
        for i in data:
            data[data.index(i)] = int((i[0] + i[-1]))
        return sum(data)


def sol1_part2():
    with open('File1') as f:
        data = f.readlines()
        for i in data:
            data[data.index(i)] = i.rstrip('\n')
        nums = {
            "1": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }
        sum = 0
        for lines in data:
            nl = []
            for i in range(len(lines)):
                for k, v in nums.items():
                    if lines[i:].startswith(k):
                        nl.append(nums[v])
            data[data.index(lines)] = nl
        for i in data:
            sum+= int(i[0])*10 + int(i[-1])

        return sum

