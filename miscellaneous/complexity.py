
text = input('Please enter your text to analyse: ')
words = text.split()
print(words)
alphanumeric = ''
letters = ''
for word in words:
    letters += word
for letter in letters:
    if letter.isalnum():
        alphanumeric += letter
    else:
        continue
print(alphanumeric)
complexity = len(alphanumeric) / len(words)
print(f'The complexity of sentence is: {complexity:.2f} letter/word')
