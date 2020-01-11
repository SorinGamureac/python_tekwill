#Write a program that will count number of lines in a file
with open("file.txt") as f:
    count_line = 0
    for line in f:
        count_line +=1
    print(count_line)
