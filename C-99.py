import os
import shutil

# function to create and transfer files
def create():
    print('** This function will transfer data from first file into the second file **\n')
    directory = input('Enter name of your directory: ')

    # creates a path along with the directory
    path = '/Users/kuber/' + directory

    # checks if the path exists, if not then it creates one
    if os.path.exists(path) == False:
        os.mkdir(path)
    
    # lists the content present in the directory
    print(os.listdir(path))

    # takes input of the file names to be created, copied, or moved
    file1 = input('Enter first file name: ')
    file2 = input('Enter second file name: ')

    # source becomes first file location 
    source = path + '/' + file1
    # destination becomes second file location
    destination = path + '/' + file2

    # checks if the source and destination
    # if not then it creates those files and takes input and adds the data
    if os.path.exists(source) == False:
        # opens file in writing mode i.e. 'w'
        fileOpen1 = open(source, 'w')
        fileData1 = input('Enter your data for first file: ')
        fileOpen1.write(fileData1)

    if os.path.exists(destination) == False:
        fileOpen2 = open(destination, 'w')
        fileData2 = input('Enter your data for second file: ')
        fileOpen2.write(fileData2)

    # again lists contents present in the directory
    print(os.listdir(path))

    # asks for choice to rather copy, move or let 
    choice = input('Would you like to copy or move or exit(c/m/e): ')
    if choice == 'c':
        shutil.copy(source, destination)
        print('Copied')
    elif choice == 'm':
        shutil.move(source, destination)
        print('Moved')
    elif choice == 'e':
        print('Created')
    else:
        print('Invalid input')
        choice = input('Would you like to copy or move(c/m): ')

# function to remove files or folders(empty ones on the desktop)
def remove():
    print('** This function will delete files or folders from desktop **\n')
    folderOrFile = input('Delete folder or file: ')

    # if wants to delete folder
    if folderOrFile == 'folder':
        directory = input('Enter the name of your directory which is empty: ')

        # creates path along with the directory name entered
        path = '/Users/kuber/' + directory
        # checks if the path exists, if not then creates one
        if os.path.exists(path) == False:
            os.mkdir(path)

        # choice for deleting permanently or in trash
        permanantOrTrash = input('Delete permanantly or move in trash(p/t): ')

        # if permanently then gone
        if permanantOrTrash == 'p':
            os.rmdir(path)
            print('Folder deleted permanently')
        # if trash
        elif permanantOrTrash == 't':
            # checks for folder named trash on the desktop, if not then creates one
            if os.path.exists('/Users/kuber/desktop/trash/') == False:
                os.mkdir('/Users/kuber/desktop/trash')
            source = path
            destination = '/Users/kuber/desktop/trash/'
            # moves the desired folder to trash
            shutil.move(source, destination)
            print('Folder Trashed')
    # if wants to delete file
    elif folderOrFile == 'file':
        directory = input('Enter the name of your directory: ')

        # creates path and lists the content present in the path
        path = '/Users/kuber/' + directory
        print(os.listdir(path))

        fileName = input('Enter the name of your file for deleting: ')

        source = path + '/' + fileName

        # checks if the file exists if not then creates one and takes input data
        if os.path.exists(source) == False:
            # opens file in writing mode i.e. 'w'
            fileOpen = open(source, 'w')
            fileData = input('Enter your data for first file: ')
            fileOpen.write(fileData)
        # again lists the content present in the path
        print(os.listdir(path))

        permanantOrTrash = input('Delete permanantly or move in trash(p/t): ')

        # if permanent then gone
        if permanantOrTrash == 'p':
            os.remove(source)
            print('File deleted permanently')
        #if trash
        elif permanantOrTrash == 't':
            # checks for a folder named trash on the desktop, if not then creates one
            if os.path.exists('/Users/kuber/desktop/trash/') == False:
                os.mkdir('/Users/kuber/desktop/trash')
            destination = '/Users/kuber/desktop/trash/'
            shutil.move(source, destination)
            print('File Trashed')

# action for calling specific function
action = input('Would you like to transfer or delete or exit(t/d/e): ')

# while loop till wants to exit
while action != 'e':
    action = input('Would you like to transfer or delete or exit(t/d/e): ')

    if action == 't':
        create()
    elif action == 'd':
        remove()
if action == 'e':
    print('Bye')