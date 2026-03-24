def rev_string(string):
    rev_string = ""
    if string.strip():
        for i in string[::-1]:
            rev_string += i

    return rev_string


text = rev_string("This is a string")
print(text)
