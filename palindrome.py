str1=input("enter string value:")
Str2=""
for i in str1:
  str2=i+str2
  if(str1==str2):
    print("palindrome ")
  else:
    print("not palindrome ")
