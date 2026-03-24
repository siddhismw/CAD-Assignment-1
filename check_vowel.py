def check_char(string):
    vowel = ('a', 'e', 'i', 'o', 'u')
    string = string.lower()
    if string.strip():
        for check in string.split():
            if check[0] in vowel:
                return "Vowel"
            else:
                return "Consonents"
