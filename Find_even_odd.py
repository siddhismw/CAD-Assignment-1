def check_number(value):
    try:
        num = int(value)
    except Exception:
        print("Invalid input")

    if num % 2 == 0:
        return "Even number"
    else:
        return "Odd number"

number = check_number(5)
print(number)
