word = input('please enter a word: ')
vowels = ['a', 'e', 'i', 'o', 'u']
num = 0
vowelCount = 0

while num < len(word):
    letter = word[num]
    if(letter in vowels):
        vowelCount += 1
    num += 1

print(vowelCount)