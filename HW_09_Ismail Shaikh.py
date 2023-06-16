"""
Ismail Shaikh
CS 100 Section 015
HW 9, November 9, 2022
"""
import string
#Problem 1
def file_copy(in_file,out_file):
    in_file=open(in_file, "r")
    out_file=open(out_file, "w")
    out_file.write(in_file.read())
    in_file.close()
    out_file.close()
#Problem 2
def file_stats(in_file):
    in_file=open(in_file)
    lines=0
    words=0
    characters=0
    for line in in_file:
        lines+=1
        words=line.split()
        for word in words:
            words+=1
        for character in line:
            characters+=1
    print("Number of lines:",lines)
    print("Number of words:", words)
    print("Number of characters:", characters)
#Problem 3
in_File=" "
out_File=" "
def repeat_words(in_File,out_File):
    in_File=open(in_File,"r")
    lines=in_File.readlines()
    out_File=open(out_File,"w")
    for line in lines:
        repeatwords=[]
        for word in line.strip().split():
            word= word.strip().lower()
            if word not in repeatwords:
                repeatwords.append(word)
            if len(repeatwords)>0:
                out_File.write("\n")
    in_File.close()
    out_File.close()
    
        
            
