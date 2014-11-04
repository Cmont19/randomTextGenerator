"""
Simple program that generates a random text file
Allows user to enter the amount of lines in the text file, and
the amount of characters per line
Allows user to specify whether they want to include all letters, or allow
numbers, special characters, etc

By default saves program to the directory where the python file is saved
"""

import string
import random

YES_OR_NO_CHOICES = ['y', 'n']

#validation for if file name is correct
def validTxtFile(fileName):
  return fileName[-4:] == ".txt"

#the function to call if all specials, digits are allowed
def generateFileAll(fileName, chars, lines):
  myFile = open(fileName, 'w')
  currentLine = 0
  writeString = ""
  while currentLine < lines:
    currentChar = 0
    newLine = ""
    while currentChar < chars:
      newLine += random.choice(string.ascii_letters + string.digits +\
                               string.punctuation)
      currentChar += 1
    writeString += newLine + '\n'
    currentLine += 1
  myFile.write(writeString)
  myFile.close()

#function to call if only chars are allowed
def generateFileChars(fileName, chars, lines):
  myFile = open(fileName, 'w')
  currentLine = 0
  writeString = ""
  while currentLine < lines:
    currentChar = 0
    newLine = ""
    while currentChar < chars:
      newLine += random.choice(string.ascii_letters)
      currentChar += 1
    writeString += newLine + '\n'
    currentLine += 1
  myFile.write(writeString)
  myFile.close()

#function to call if only letters and special characters are allowed
def generateFileSpec(fileName, chars, lines):
  myFile = open(fileName, 'w')
  currentLine = 0
  writeString = ""
  while currentLine < lines:
    currentChar = 0
    newLine = ""
    while currentChar < chars:
      newLine += random.choice(string.ascii_letters + string.punctuation)
      currentChar += 1
    writeString += newLine + '\n'
    currentLine += 1
  myFile.write(writeString)
  myFile.close()

#function to call if only letters and digits are allowed
def generateFileDigits(fileName, chars, lines):
  myFile = open(fileName, 'w')
  currentLine = 0
  writeString = ""
  while currentLine < lines:
    currentChar = 0
    newLine = ""
    while currentChar < chars:
      newLine += random.choice(string.ascii_letters + string.digits)
      currentChar += 1
    writeString += newLine + '\n'
    currentLine += 1
  myFile.write(writeString)
  myFile.close()
  
  

def main():
  
  keepGenerating = "yes"
  while(keepGenerating):
    
    #get the file name for the user/check to make sure it has .txt extension
    fileName = input("Enter the name to save the random text file as: ")
    while not validTxtFile(fileName):
      fileName = input("Please enter a valid name ending in .txt: ")

    #get the amount of lines for the random file
    numLines = input("Enter the number of random lines to write: ")
    while not numLines.isdigit():
      numLines = input("Please enter an integer value only for the number " +\
                       "of lines: ")
      
    #get the amount of characters per line for the random file
    charsPerLine = input("Enter the number of characters to write per line: ")
    while not charsPerLine.isdigit():
      charsPerLine = input("Please enter an integer value only for the " +\
                           "number of characters per line: ")

    #get input about special characters/digits/spaces being allowed
    specials = False
    digits = False
    allowSpecials = input("Enter 'y' to allow special characters, 'n' to " +\
                          "not allow specials: ")
    while not allowSpecials in YES_OR_NO_CHOICES:
      allowSpecials = input("Please only type 'y' or 'n': ")
    if(allowSpecials == 'y'):
      specials = True
    allowDigits = input("Enter 'y' to allow digits, 'n' to not allow digits: ")
    while not allowDigits in YES_OR_NO_CHOICES:
      allowDigits = input("Please only type 'y' or 'n': ")
    if(allowDigits == 'y'):
      digits = True

    #generate the file
    if(specials and digits):
      #print("all allowed")
      generateFileAll(fileName, int(charsPerLine), int(numLines))
    elif(specials):
      generateFileSpec(fileName, int(charsPerLine), int(numLines))
    elif(digits):
      generateFileDigits(fileName, int(charsPerLine), int(numLines))
    else:
      #print("only chars")
      generateFileChars(fileName, int(charsPerLine), int(numLines))

    #allow user to keep generating random files
    keepGenerating = input("Enter any character to generate another file " +\
                           "or press <Enter> to quit: ")

main()
