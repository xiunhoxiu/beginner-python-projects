def translation():
    phone = input("Phone: ")
    return f" testing if it works {number(phone)}"


def number(x):
    digits_mapping = {
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine"
    }
    output = ""
    for phoneNumber in x:
        output += digits_mapping.get(phoneNumber, "!") + " "
    return output


print(translation())

