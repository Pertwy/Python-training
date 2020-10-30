monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April"
}

print(monthConversion["Jan"])
#print(monthConversion.get("Qwe", "Not a valid key"))

names = ([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'},
          {'name': 'Homer'}, {'name': 'Marge'}])


def namelist(names):
    for key in names.items():
        print(key, "->",  names[key])


namelist(names)
