from collections import Counter

all_emails =  ""

while True:
    print("      | sample phishing email common word finder |       ")
    n = 0
    while n <= 10 :
        email_text = input(f"PLease paste your {n} email content :")
        all_emails += f" {email_text} "
        n+=1
    break

words = all_emails.replace("  "," ").split(" ")

most_occuring_words = Counter(words) # this will give you a list in return , remember !!

top_most_words = most_occuring_words.most_common(10) # fetches the top 10 words with highest frequency 

for word, frequency in top_most_words:
    print("\n \n | Results |")
    print(f" '{word}' has occured {frequency} times")


    