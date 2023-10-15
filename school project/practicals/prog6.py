
consonants_upper = 0
vowels = 0
lower_chars = 0

VOWELS = 'aeiou' 

with open(r'C:\Users\maste\OneDrive\Desktop\phyton programming\school project\practicals\data.txt','r') as f:
  
  for line in f:
    for char in line:
      if char.isupper() and char not in VOWELS:
        consonants_upper += 1
      elif char in VOWELS:
        vowels += 1
      elif char.islower():
        lower_chars += 1

print("Consonant upper case letters:", consonants_upper) 
print("Vowels:", vowels)
print("Lower case characters:", lower_chars)