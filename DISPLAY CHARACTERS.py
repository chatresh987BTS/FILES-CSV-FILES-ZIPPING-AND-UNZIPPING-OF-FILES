CREATE A FILE NAMED SAMPLE1.TXT WITH SOME TEXT AND COUNT THE NUMBER OF VOWELS , CHARACTERS , LINES , WORDS IN FILE. 
f = open("sample1.txt", "r")
text = f.read()
f.close()
char_count = 0
word_count = 0
vowel_count = 0
line_count = 0
for char in text:
    char_count = char_count + 1
    if char.lower() in "aeiou":
        vowel_count = vowel_count + 1
words_list = text.split()
word_count = len(words_list)
lines_list = text.splitlines()
line_count = len(lines_list)
print("Characters:", char_count)
print("Words:", word_count)
print("Vowels:", vowel_count)
print("Lines:", line_count)
