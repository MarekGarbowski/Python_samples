
text = input('Please enter your text to analyse: ')
words = text.split()
alphanumeric = ''
for letter in text:
    if letter.isalnum():
        alphanumeric += letter
    else:
        continue
complexity = len(alphanumeric) / len(words)
print(f'The complexity of sentence is: {complexity:.2f} letter/word')
