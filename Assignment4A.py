
def format_word(word):
    capitalized = word.upper()
    pascalword = ""
    first = True
    for ch in capitalized:
        if first == False:
            pascalword += ch.lower()
        else:
            pascalword += ch.upper()
            first = False
    return(pascalword)
def convert_to_pascal_case(text):
    word = ""
    pascaltext = ""
    for ch in text + " ":
        if ch != " ":
            word += ch.lower()
        else:
            pascaltext += format_word(word)
            word = ""
    return(pascaltext)
string = input("Enter a string: ")
pascaltext = convert_to_pascal_case(string)
print(f"Pascal Case: {pascaltext}")





