filename = r'C:\Users\maste\OneDrive\Desktop\phyton programming\school project\practicals\data.txt'

with open(filename) as file:
  for line in file:
    words = line.strip().split()
    
    print('#'.join(words))

