words = "alksncdcs"

for letter in words:
    print(letter)


arrays = ["dasd", "a", "g", "o"]

for element in arrays:
    print(element)


for index in range(10):
    print(index + 1)

for index in range(5, 8):
    print(index)

for index in range(len(arrays)):
    print(arrays[index])


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            translation = translation + "o"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a Phrase")))
