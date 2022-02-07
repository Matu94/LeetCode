wovels = "aeiou"

sentence = "i dont remember what was the sentence, but this will be fine"

result = {}

for letter in sentence:
    if letter in wovels:
        # .get() method returns the value of the item with the specified key. 0 is the default result if there is no match
        result[letter] = result.get(letter, 0) + 1
        
print(result)