def AlphabetSoup(str):
  array = []
  output = ""

  for char in str:
    array.append(char)
    
  array = sorted(array)

  for char in array:
    output += char
  
  return output

# keep this function call here 
print(AlphabetSoup(input()))