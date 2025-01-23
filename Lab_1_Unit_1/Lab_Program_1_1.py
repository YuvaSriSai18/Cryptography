import string

file = open('textFile.txt', 'r')
content = file.read()  
file.close() 

letters = string.ascii_letters
dic1 = {}
for i in letters:
    dic1[i] = 0

for char in content:
    if char in letters:
        dic1[char] += 1

print('\n Character Frequency in the given text file : \n')
print(dic1)

print('\n\n ASCII Values : \n')
keys_list = list(dic1.keys())
for letter in keys_list:
    print(f'{letter} : {ord(letter)}')