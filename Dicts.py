roll_number = {
    1 : "Sanskriti",
    15 : "Shabbar Abbas Zaidi",
    20 : "Shambik Thakur",
    45 : "Shreyash"
    }

clg_mail = {
    "Shambik Thakur" : "shambik@bbdu.ac.in",
    "Sanskriti" : "sanskriti@bbdu.ac.in",
    "Shabbar Abbas Zaidi" : "shabbar@bbdu.ac.in",
    "Shreyash" : "shreyash@bbdu.ac.in"
}

def fetch_mail(roll_number, clg_mail):
    for x, y in roll_number.items():
        for a, b in clg_mail.items():
            if y == a:
                print(x, y, b)


fetch_mail(roll_number, clg_mail)
