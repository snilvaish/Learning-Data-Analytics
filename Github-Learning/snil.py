def ReverseString(word):
  token_list=word.split()
  str=""
  for i in token_list:
    length=len(i)-1 
    for j in i:
        f="".join(i[length])
        str=str+f
        length= length-1
    str=str+" "
  return str    
print(ReverseString("I love INDIA"))

