import json

text = input('Enter the text what you want to be translated into Morse code:')

length = len(text)

with open('input/alphabet.json') as f:
    data = json.load(f)
    
    for i in range(length):
        for j in data['letters']:
            if (i == j):
                print(i)


print(data['letters']['a'])
print("\n")
print(data['numbers'])

