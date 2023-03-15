import os
#this_path = os.getswd

def word_count(file_content):
    word_list = file_content.split()
    return len(word_list)

def char_dict(file_content):
    word_list = file_content.split()
    char_dict = dict()
    for word in word_list:
        for char in word.lower():
            if char in char_dict.keys():
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

with open(r'/home/reo3-0/workspace/github.com/reo3-0/bookbot/books/frankenstein.txt') as f:
    file_content = f.read()

print("--Begin report of books{file_name}--".format(file_name=f.name[f.name.rfind('/'):]))
print("{words} words found in the document\n".format(words=word_count(file_content)))

this_char_dict = char_dict(file_content)
tuple_list = sorted(this_char_dict.items(), key=lambda x: x[1], reverse=True) #dict.items() returns list of tuples
for word_counts in tuple_list:
    if word_counts[0].isalpha():
        print("The {letter} character was found {n} times".format(letter=word_counts[0],n=word_counts[1]))