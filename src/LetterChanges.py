import string

def isVowel(str):
    temp = str.lower()
    return temp in 'aeiou'

def LetterChanges(str):
    output = ""
    for char in str:
      if(char.isalpha()):
        char = string.ascii_letters[string.ascii_letters.index(char) + 1]
        if(isVowel(char)):
          char = char.upper()
      output += char
    return output

# keep this function call here 
print(LetterChanges(input()))