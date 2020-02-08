def FindIntersection(strArr):
  #definitions
  a_set = strArr[0].split(", ")
  b_set = strArr[1].split(", ")
  output = ""
    
  #find intersection
  for number in a_set:
    if(number in b_set):
        output = output + str(number) + ','
  
  #return output
  length_output = len(output)
  if(length_output > 0):
    #remove last comma
    return output[:length_output-1]
  else:
    return False

# keep this function call here 
print(FindIntersection(input()))