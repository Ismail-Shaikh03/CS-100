"""
Ismail Shaikh
CS 100 Section 015
HW 12, December 12, 2022
"""
#Problem 1
def safeOpen(filename):
    try:
        open_File=open(filename)
        return open_File
    except FileNotFoundError:
        return None
#Problem 2
def safeFloat(x):
    try:
        float_num=float(x)
        return float_num
    except:
        return 0.0
    
#Problem 3
def averageSpeed():
    try:
        filename=input("Enter the file name you would like to open:")
        inputFile=safeOpen(filename)
        if inputFile == None:
            print("There's no file named:"+ filename + "You have one more attempt")
            file=input("Enter the file name you would like to open:")
            inputFile=safeOpen(filename)
    except:
       print("File isn't found. That's your last try. Goodbye!")
    read_file=inputFile.readlines()
    average_speed= []
    for num in read_file:
        lines=num.split()
        for i in lines:
            if safeFloat(i) and float(i)> 1:
                average_speed.append(float(i))
    average=sum(average_speed)/len(average_speed)
    print("Average speed:"+ str(average)+ "miles per hour.")
    
