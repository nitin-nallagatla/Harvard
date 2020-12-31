# Imports libraries.
import cs50

# Gets Input.
text = cs50.get_string("Text: ")

# Intializes variables.
letterCount = 0

# Checks letter count.
for letter in text:
    if letter.isalnum() == True:
        letterCount += 1

# Checks word count.
wordCount = len(text.split())

# Checks sentence count.
sentenceCount = 0
for sentence in text:
    if sentence == '.' or sentence == '?' or sentence == '!':
        sentenceCount += 1

# Creates average variables.
aveLettersPer100Words = letterCount * (100 / wordCount)
aveSentencesPer100Words = sentenceCount * (100 / wordCount)

# Calculate grade level.
gradeLevel = (.0588 * aveLettersPer100Words) - (.296 * aveSentencesPer100Words) - 15.8

# Returns grade level.
if gradeLevel < 0:
    print("Before Grade 1")
elif gradeLevel > 16:
    print("Grade 16+")
else:
    print("Grade", round(gradeLevel))