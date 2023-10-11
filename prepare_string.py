def stringFormater(value):
    new_value = ""
    value = value.replace(" + ", "+")
    value = value.replace(" = ", "=")

    for char in value:
        if char == "+":
            new_value += "#"
        elif char == "'":
            last_letter = new_value[-1]
            new_value = new_value[:-1] + f'!{last_letter}'
        elif char == " ":
            new_value += '&'
        else:
            new_value += char
    return new_value