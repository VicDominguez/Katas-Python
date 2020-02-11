def cleaner(word):
    output = ""
    for char in word:
        if(char.isalnum()):
            output += char
    return output

def LongestWord(sen):
    words = sen.split(" ") #take words from string
    
    #variables for iterate the list of words
    index = 0
    max_length_index = 0
    max_length_found = -1
    
    for index in range(len(words)):
        words[index] = cleaner(words[index]) #clean word
        if(len(words[index]) > max_length_found): #pick the longest word
          max_length_found = len(words[index])
          max_length_index = index

    return words[max_length_index]

# keep this function call here 
print(LongestWord(input()))