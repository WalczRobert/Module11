addr_file = open ("data/addr_book.txt")
for line in addr_file:
    print (line)
addr_file.close ()

a = "Hello, You!"
print(a.lower())
print(a.upper())

a = "This is a great day to learn about programming."
b = a.find("great")
c = a.find("blue")
print(b)
print(c)

a = "This is a great day to learn about programming."
b = a.replace("great", "beautiful").upper().split(" ")
print (b)