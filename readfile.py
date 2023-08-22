# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 15:30:32 2023

@author: Students
"""

File=open("demo.txt","r")
print(File.read())

File1=open("demo.txt","w")
a=File1.write("Hello to Everyone")
print(File.read())

File2=open("demo.txt","a")
print(File2.write(" DYPATIL"))
print(File.read())

lines=["Hello World\n","Welcome to DyPatil Akurdi, Pune\n"]
File3=open("demo.txt","w")
File3.writelines(lines)
File3.close()
print(File.read())


fileptr=open("demo.txt","r")
print("The Filepointer is at Byte",fileptr.tell())

content=fileptr.read()
fileptr.seek(10)
print("After reading the file pointer is at",fileptr.tell())


#hello 