def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    numberOfWords = getNumberofWords(text)
    characterCounts = charCounts(text)
    alphaCount = checkAlpha(characterCounts)
    printResult(alphaCount)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def getNumberofWords(text):
    return len(text.split())

def charCounts(text):
    chars_dict = {}
    lowered_string = text.lower()
    for i in lowered_string:
        if i in chars_dict:
            chars_dict[i] += 1
        else:
            chars_dict[i] = 1
    return chars_dict

def checkAlpha(dict):
    isAlpha = {}
    #print(list(dict.keys())[2].isalpha())
    for i in dict:
        if i.isalpha():
            isAlpha[i] = dict[i]

    return sorted(isAlpha.items(), key=lambda item:item[1], reverse=True)

def printResult(tuples):
    for i in tuples:
        print(f"The '{i[0]}' character was found {i[1]} times")

main()