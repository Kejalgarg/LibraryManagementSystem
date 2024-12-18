
import os
import csv


#adding books

def newBook():
    print("Add a New Book Record")
    print("========================")
    file = open('Library.csv','a',newline='\r\n')
    fileWriter = csv.writer(file)
    bookId = int(input('Enter Book Id='))
    bookName = input('Enter Book Name=')
    cost = float(input('Enter Cost='))
    author = input('Enter Author=')
    rec = [bookId,bookName,author,cost]
    fileWriter.writerow(rec)
    file.close()
    print("Record Saved...")


#updating data of existing books

def updateBook():
    print("Modify a Book Record")
    print("=======================")
    file=open('Library.csv','r',newline='\r\n')
    tempFile=open('temporary.csv','w',newline='\r\n')
    targetBookId=input('Enter Book Id of Book you want to modify:  ')
    fileReader=csv.reader(file)
    tempFileWriter=csv.writer(tempFile)

    # for finding the record to be modified

    for rec in fileReader:
        if rec[0]==targetBookId:
            print("Record Found!")
            print("BookId=",rec[0])
            print("BookName=",rec[1])
            print("Author=",rec[2])
            print("Cost=",rec[3])
            choice=input("Do you want to modify..?(y/n)=")

            # for updating book record

            if choice.lower() == 'y':
                bookId = int(input('Enter New BookId='))
                bookName = input('Enter new Book Name=')
                author = input('Enter Author=')
                cost = float(input('Enter Cost='))
                rec = [bookId,bookName,author,cost]
                print("Record Modified...")
            else:
                print("Record Not Modified...")
        tempFileWriter.writerow(rec)
    else :
        print("Record NOT Found!")

    # Closing Files
    file.close()
    tempFile.close()
    os.remove("Library.csv")
    os.rename("temporary.csv","Library.csv")


#deleting books

def deleteBook():
    file=open('Library.csv','r',newline='\r\n')
    tempFile=open('temporary.csv','w',newline='\r\n')
    targetBookId=input('Enter BookId of Book you want to delete=')
    fileReader=csv.reader(file)
    tempFileWriter=csv.writer(tempFile)

    # for finding the record to be deleted

    for rec in fileReader:
        if rec[0]==targetBookId:
            print("BookId=",rec[0])
            print("Book Name=",rec[1])
            print("Author=",rec[2])
            print("Cost=",rec[3])
            choice=input("Do you want to delete this record(y/n)=")

            #for deleting book

            if choice.lower()=='y':
                print("Record Deleted...")
                continue
        tempFileWriter.writerow(rec)
    else :
        print("No such record found...")

    # Closing Files
    file.close()
    tempFile.close()
    os.remove("Library.csv")
    os.rename("temporary.csv","Library.csv")


# searching the required book

def searchBook():
    print("Search a Record")
    print("===================")
    file=open('Library.csv','r',newline='\r\n')
    targetBookId=input('Enter BookId you want to search=')
    fileReader=csv.reader(file)

    # for finding the record to be searched

    for rec in fileReader:
        if rec[0] == targetBookId:
            print("BookId=",rec[0])
            print("Book Name=",rec[1])
            print("Author=",rec[2])
            print("Cost=",rec[3])
        else:
            print("No such record found...")
    file.close()
    input("Press any key to continue..")


# Listing all books in the library

def listBooks():
    print("List of All Books")
    print("===================")
    file = open('Library.csv','r',newline='\r\n')
    fileReader = csv.reader(file)
    for rec in fileReader:
        print(rec[0],end="\t\t")
        print(rec[1],end="\t\t")
        print(rec[2],end="\t\t")
        print(rec[3])
    file.close()


# Information about the project

def info() :
  print("This project was developed by:")
  print("Kejal garg")
  print("Roll No: 18")
  print("Class: XII-J")
  print("as a submission for CBSE Computer Science Final Project.")
  print("Submitted To: Mr. Mohitendra Dey")


# Menu for executing various functions

def main():
    while True:

        print("\n\n====================================")
        print("Library Management System by Kejal Garg")
        print("====================================")
        print("\n==========")
        print("Main Menu")
        print("==========")
        print("1. Add a new Book Record")
        print("2. Modify Existing Book Record")
        print("3. Delete Existing Book Record")
        print("4. Search a Book Record")
        print("5. List of all Books")
        print("6. Information about Project")
        print("7. Quit")

        choice = int(input('Enter your choice:  '))

        if choice==1:
            newBook()
        elif choice==2:
            updateBook()
        elif choice==3:
            deleteBook()
        elif choice==4:
            searchBook()
        elif choice==5:
            listBooks()
        elif choice==6:
            info()
        elif choice==7:
            print("Bye !!")
            break
        else :
            print("INCORRECT OPTION, TRY AGAIN !!!")
main()
