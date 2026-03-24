def check_prime(variable):
    try:
        check = int(variable)
    except Exception:
        print("Invalid input")

    if check <= 1:
        return "Not prime"

    for i in range(2, int(check**0.5) + 1):
        if check % i == 0:
            return "Not prime"
    return "Prime number"

var = check_prime(8)
print(var)
