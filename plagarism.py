'''
A plagiarism checker is a tool or software 
used to detect instances of plagiarism in written content.
 Plagiarism refers to the act of using someone else's work, ideas, or words without proper attribution,
 which is unethical and can have serious consequences, especially in academic and professional settings.'''
#first import datd and sequencematcher is used to check two textfile data
from difflib import SequenceMatcher

#open two textfiles textfile.txt&textfile2.txt
with open("textfile1.txt") as file1,open("textfile2.txt")as file2:

#read files1 data & file2 data
    f1data=file1.read()
    f2data=file2.read()

#create variable and place sequencematche and sequencematcher has some parameters check how mach data is matched and ratio()function is used to display the output in ratio format so,
    percentage=SequenceMatcher(None,f1data,f2data).ratio()

#we use persentage*100 is convert ratio format to percentage
    print("Similarity of two text files :",round(percentage*100,2),"%")

