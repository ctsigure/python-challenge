import os
import string
import re


fptxt = os.path.join(os.path.dirname(__file__),"raw_data","paragraph_1.txt")


f = open(fptxt, "r")
content = f.read()

word = content.split()
word_count = len(word)

sentence = re.split("(?<=[.!?]) +", content)
sentence_count = 0
for i in sentence:
    if i != "":
        sentence_count += 1

letter = list(content)
letter_count = 0
for j in letter:
    if j not in string.punctuation:
        letter_count += 1

average_letter_count = letter_count / word_count 
average_sentence_length = letter_count / sentence_count





print("Paragraph Analysis" + '\n'+'-' * 25 + '\n' +
"Approximate Word Count: " + str(word_count) + '\n' +
"Approximate Sentence Count: " + str(sentence_count) + '\n' +
"Average Letter Count: " + str(average_letter_count) + '\n' +
"Average Sentence Length: " + str(average_sentence_length))