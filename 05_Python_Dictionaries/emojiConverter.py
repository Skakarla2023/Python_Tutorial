message = input(">")
words = message.split(' ')
# this method goes upto the space that we have specified and uses it as boundary to split the words in the given string and then it returns a list

emojis={
    ":)":"😊",
    ":(":"😒"
}

output = " "
for word in words:
    output += emojis.get(word, word)+" "

print(output)

