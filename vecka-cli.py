import urllib.request


def get_digit(string: str) -> int:
    if string == "ett":
        return 1
    elif string == "två":
        return 2
    elif string == "tre":
        return 3
    elif string == "fyra":
        return 4
    elif string == "fem":
        return 5
    elif string == "sex":
        return 6
    elif string == "sju":
        return 7
    elif string == "åtta":
        return 8
    elif string == "nio":
        return 9

    raise ValueError("")


def get_week(string: str) -> int:
    week: int = 0
    digit: str = None

    if string == "tio":
        return 10
    elif string == "elva":
        return 11
    elif string == "tolv":
        return 12
    elif string[-3:] == "ton":
        substring = string[:-3]
        week += 10

        if substring == "tret":
            return 13
        elif substring == "fjor":
            return 14
        elif substring == "sjut":
            return 17
        elif substring == "ar":
            return 18
        elif substring == "nit":
            return 19
        else:
            digit = substring
    elif string[:5] == "tjugo":
        week += 20
        digit = string[5:]
    elif string[:7] == "trettio":
        week += 30
        digit = string[7:]
    elif string[:6] == "fyrtio":
        week += 40
        digit = string[6:]
    elif string[:6] == "femtio":
        week += 50
        digit = string[6:]

    if digit is None:
        digit = string
    elif digit == "":
        return week

    return week + get_digit(digit)


response = urllib.request.urlopen("https://vecka.vikekh.com/week")
week = response.read().decode("utf-8")
print(get_week(week))

# test = ["ett", "två", "tre", "fyra", "fem", "sex", "sju", "åtta", "nio",
#         "tio", "elva", "tolv", "tretton", "fjorton", "femton", "sexton", "sjutton", "arton", "nitton",
#         "tjugo", "tjugoett", "tjugotvå", "tjugotre", "tjugofyra", "tjugofem", "tjugosex", "tjugosju", "tjugoåtta", "tjugonio",
#         "trettio", "trettioett", "trettiotvå", "trettiotre", "trettiofyra", "trettiofem", "trettiosex", "trettiosju", "trettioåtta", "trettionio",
#         "fyrtio", "fyrtioett", "fyrtiotvå", "fyrtiotre", "fyrtiofyra", "fyrtiofem", "fyrtiosex", "fyrtiosju", "fyrtioåtta", "fyrtionio",
#         "femtio", "femtioett", "femtiotvå", "femtiotre"]

# for week in test:
#     print(get_week(week))