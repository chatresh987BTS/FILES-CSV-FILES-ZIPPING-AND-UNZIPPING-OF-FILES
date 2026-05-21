REVERSE THE CONTENT OF THE TEXT FILE.
f1 = open("source.txt", "r")
text = f1.read()
f1.close()
reversed_text = text[::-1]
f2 = open("destination.txt", "w")
f2.write(reversed_text)
f2.close()
print("File successfully reversed!")
f=open("destination.txt",'r')
l=f.readlines()
print(l)
