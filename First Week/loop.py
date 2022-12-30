# While loop example

sum = 0
i = 1

while i < 10:
    sum += i
    i += 1

print("Sum:",sum, "count:", i)


# for loop example

for i in range(1, 9, 3):
    print(i)
    
name = "Python"

for letter in name:
    print(letter)

for letter in range(len(name)):
    print(name[letter])
    
words = ['cats', 'dogs', 'sharks']
for word in words:
    print(word)                     
    
 