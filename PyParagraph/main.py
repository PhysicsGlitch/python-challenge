# Overview: The basic task is to "tokenize" the text into discrete words to analyze.
# The steps to do this are as follows:
# Step 1: Convert the Text file into a list of discrete words.
# Step 2: Analyze the words and record results.
# Step 3: Write the results to a text file.

import os

text = open(os.path.join('Resources', 'The World Goes On.txt'))
raw_list = list(text.readlines())

# The three steps below clean the data from the raw_list converted using the vanilla text reader.
# The first step gets rid of the new line marker in the file with the replace method.
# The second step splits the words using the split method.
# The third step uses a nested for loop to flatten out the lists. They were broken into a list of lists
# because of the line break and the nested for loop creates one main list of all the words.

line_list = [word.replace("\n", "") for word in raw_list]
word_list = [word.split() for word in line_list]

words = []
for i in word_list:
    for j in i:
        words.append(j)

word_count = len(words)

# I read the wikipedia on regular expressions. Many of the words have a , or ., attached to them. I manually
# adjusted for that in the analysis. Although, knowing how to split them out using regex is helpful.
# For this first week I have been trying to do everything in vanilla as much as possible without importing things.
# I made a pseudo regular expression counter by just incrementing the commas and periods. An imperfect method
# because it ignores ' and other marks. But it gives an approximate number of characters to remove from my character
# count and the sentences. This method would break if there were periods in titles or suffixes (e.p. Mr., Jr., M.D.).

sentence_count = 0
comma_count = 0
for word in words:
    for a in word:
        if a == '.':
            sentence_count += 1
        elif a == ',':
            comma_count += 1

character_count = 0
for word in words:
    character_count += len(word)

# Average letter count of words deletes the number of periods and commas to give an approximate letters/words.
average_letter_count = (character_count - sentence_count - comma_count)/word_count

# I didn't realize this was basically a paragraph sentence before I started analyzing.
# Probably shouldn't have chosen an esoteric Hungarian writer in translation ...

average_sentence_count = word_count/sentence_count

print("Paragraph Analysis")
print("-----------------")
print(f"Approximate Word Count: {word_count}")
print(f"Approximate Sentence Count: {sentence_count}")
print(f"Average Letter Count: {round(average_letter_count, 2)}")
print(f"Average Sentence Length: {average_sentence_count}")

# Creates a path to the results text file.
analysis = os.path.join("analysis.txt")

# I used formatted strings and \n to create new lines to print a basic text file.

with open(analysis, "w") as datafile:

    datafile.write(f"Paragraph Analysis\n")
    datafile.write(f"-----------------\n")
    datafile.write(f"Approximate Word Count:{word_count}\n")
    datafile.write(f"Approximate Sentence Count: {sentence_count}\n")
    datafile.write(f"Average Letter Count: {round(average_letter_count, 2)}\n")
    datafile.write(f"Average Sentence Length: {average_sentence_count}\n")
