def QuestionsMarks(str):
  #definitions
  output = "true"
  sumatory_10_found = False
  length_string = len(str)
  index = 0
  sumatory = 0
  digits_found = 0
  question_mark_found = 0

  while(output == "true" and index < length_string):
    actual_char = str[index]

    if(actual_char.isdigit()):
      digits_found +=1
      
      if(digits_found > 1): #start comparing pairs
        sumatory += int(actual_char)

        #limit case
        if(sumatory_10_found == False and sumatory == 10):
          sumatory_10_found = True
        
        #search counterexample
        if(sumatory == 10 and question_mark_found != 3):
          output = "false"
        
        #restart interval
        sumatory = int(actual_char)
        question_mark_found = 0
      
      else:
        sumatory = int(actual_char)
          
    elif(actual_char == '?' and digits_found > 0): #count question mark
      question_mark_found+=1
    
    index+=1 #next iteration

  if(sumatory_10_found == False):
    output = "false"

  return output

# keep this function call here 
print(QuestionsMarks(input()))