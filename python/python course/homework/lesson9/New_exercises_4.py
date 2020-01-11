#Write a program that will remove newline character from a file.
with open('file.txt','r') as f:
    data = f.read()
    with open('file.txt','w') as delete_n:
    	delete_n.write(data.replace('\n',''))
    print(data)