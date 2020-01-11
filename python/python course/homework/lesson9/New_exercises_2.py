# #Write a program that will count frequency of a word in a file
# with open("file.txt", "r", encoding="utf-8") as f:
#     text = []
#     for line in f:
#         text.append(line)
#     # print(text)
#     count_word = {}
#     splited_words = []
#     for words in text:
#         splited_word = words.split()
#         splited_words.append(splited_word)
#     print(splited_words)
#     list_of_words = []  
#     print(len(splited_words[0])) 
#     print(len(splited_words[1])) 
#     print(len(splited_words[-1]))   
#     for splited in splited_words:
#         if len(splited) == 1:
#             list_of_words.append(splited)
#         else:
#             for new_splited in splited:
#                 list_of_words.append(new_splited)
#     print(list_of_words)
    


    # Calculeaza frecventa doar unui singur cuvant
with open("file.txt", "r") as f:
    line = f.read()
    f.seek(0)
    if "testtex" in line:
        value = line.count("testtex")
    print("Number of appearences of 'testtex' in file file.txt = %s" % value)