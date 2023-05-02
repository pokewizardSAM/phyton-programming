# string = input("Enter a string:")
# maxsub = ''
# sub = ''
# for char in string:
#     if char.lower() not in 'aeiou':
#         sub += char
#     elif len(sub) > len(maxsub):
#         maxsub = sub
        
# print("Maximum length consonant substring is :", maxsub)
# print("with", len(maxsub), "characters")

# string = input("Enter a string:")
# length = len(string)
# maxlength = 0
# maxsub =''              #empty string
# sub =''                 #empty string
# lensub = 0
# for a in range(length):
#    if string[a] in 'aeiou' or string[a] in 'AEIOU' :
#        maxsub = sub
#        maxlength = lensub
#        sub = ''
#        lensub = 0
#    else :
#        sub += string[a]
#        lensub = len(sub)
#    a += 1
# print ("Maximum length consonant substring is :" , maxsub, end = ' ')
# print ("with", maxlength, "characters")

string = input("Enter a string:")
maxlength = 0
maxsub =''              #empty string
sub =''                 #empty string
for a in string:
   if a.lower() not in 'aeiou':
       sub += a
   else:
       if len(sub)> maxlength:
           maxlength = len(sub)
           maxsub = sub
       sub = ''
print ("Maximum length consonant substring is :" , maxsub, end = ' ')
print ("with", maxlength, "characters")
