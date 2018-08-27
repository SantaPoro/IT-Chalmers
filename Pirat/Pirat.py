# def translate(word):
#     """ determines whether e is contained in the list """
#     for elem in list(word):
#         for vokal in vokaler:
#             if (vokal == elem):
#                 print (vokal)
#             else:
#                 print (elem + "o" + elem)
#
#         print (elem)




vokaler = ["a", "o", "e", "i", "u", "y", "å", "ä", "ö", " ", "," "." ":", "?", "!", "\n"]
finalWord = []

print ("Hello!, what would you like to access?")
print ("1. word translation")
print ("2. file translation")
answer = input("enter number here:")

if answer == '1':
    print ("please enter your desired word to translate")
    word = input()
    for char in list(word):
        lowerChar = char.lower()
        if (lowerChar in vokaler):
            finalWord.append(lowerChar)
        else:
            finalWord.append(lowerChar + "o" + lowerChar)


    for word in finalWord:
        print(word, end="", flush=True)
if answer == '2':
    print ("file text")
    filename = input("Enter filename: ")
    file = open(filename, 'r').read()

    print(file)

    for char in list(file):
        lowerChar = char.lower()
        if (lowerChar in vokaler):
            finalWord.append(lowerChar)
        else:
            finalWord.append(lowerChar + "o" + lowerChar)

    for word in finalWord:
        print(word, end="", flush=True)