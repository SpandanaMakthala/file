obj=open("s.txt","w+")
obj.write("Hello abhishek\n")
obj.write("my name")
obj.close()
obj=open("s.txt","r")
print(obj.read())