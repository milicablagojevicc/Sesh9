#Files: main operations = read, write
fp = open("text.txt") #this is open from reading
print(fp.read())
fp.close() #this is good practice, but not necessary - file closes anyway at the end

print(" ") #just to make it look prettier

#same thing using a context manager - MORE PYTHONIC
with open("text.txt", "r") as f: #r = read, w = write
    print(f.read())

#no need to close
print(" ")

with open("text.txt", "r") as f:
    for line in f: #f is iterable and we get each individual line
        print(line) # one enter is from print, the other one from the file

        print(line, end="")
        print(line.rstrip())