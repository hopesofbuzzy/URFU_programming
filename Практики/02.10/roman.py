

def roman_to_digit(roman: str):
    digit = 0
    while roman:
        digit += read_roman(roman)[0]
        roman = read_roman(roman)[1]
    return digit

def digit_to_roman(digit: int):
    roman = ""
    while digit:
        roman += read_digit(digit)[0]
        digit = read_digit(digit)[1]
    return roman

def read_digit(num: int):
    if num >= 50:
        return ("L", num-50)
    elif num >= 40:
        return ("XL", num-40)
    elif num >= 10:
        return ("X", num-10)
    elif num >= 9:
        return ("IX", num - 10)
    elif num >= 5:
        return ("V", num-5)
    elif num >= 4:
        return ("IV", num-4)
    elif num >= 3:
        return ("III", num-3)
    elif num >= 2:
        return ("II", num-2)

def read_roman(text: str):
    chars = ""
    r = ()
    for i, char in enumerate(text):
        chars += char
        match chars:
            case "III":
                r = (3, text[i + 1:])
            case "II":
                r = (2, text[i+1:])
            case "I":
                r = (1, text[i+1:])
            case "IV":
                r = (4, text[i+1:])
            case "V":
                r = (5, text[i+1:])
            case "IX":
                r = (9, text[i+1:])
            case "XL":
                r = (40, text[i + 1:])
            case "X":
                r = (10, text[i+1:])
            case "L":
                r = (50, text[i+1:])
    return r

print([''])

