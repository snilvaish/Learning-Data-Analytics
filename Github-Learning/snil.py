def ReverseString(word):
  token_list=word.split()
  str=""
  for i in token_list:
    length=len(i)-1
    for j in i:
        temp="".join(i[length])
        str=str+temp
        length= length-1
    str=str+" "
  return str
print(ReverseString("I love INDIA"))

