text = "This is a sample text. Here is another line."

query = input("Enter word to search: ")

lines = text.split('. ')
line_num = 1 

for line in lines:
  words = line.split()
  
  word_num = 1
  
  for word in words:
    if word == query:
      print(f"Found {query} at line {line_num}, word {word_num}")
    
    word_num += 1
  
  line_num += 1