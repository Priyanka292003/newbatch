str1=input("Enter first string:").lower()
str2=input("Enter second string:").lower()

if sorted(str1)==sorted(str2):
    print("Both strings are anagrams")
else:
    print("Both strings are not anagrams")