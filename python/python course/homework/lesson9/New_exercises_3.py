# Write a program that will append new content to the end of a file.
with open("file.txt", "a+" ) as f:
    for i in range(100):
        f.write(f'test {i}\n')
    