from itertools import count


word = input('enter a word: ')
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
for char in word:
    if char in vowels:
        count += 1
    

print(count)