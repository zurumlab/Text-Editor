import os

""" This code is written by James Chizurum Akandu
    must not be used without the owners concent.
    Date: 1/1/2022
"""


print("\n") 

print("Hi, this is CL text editor written by James Chizurum. This program let you read, create, open and  update your text documents. To open or createba file enter c. To update a file enter u. To delete a file enter d. To exit the programm enter any letter \n") 

print("\n")

text_status = "words: {}, characters: {}, last updated: {}"

try:

    file_name = input("Enter file name: \n")
    print("\n")
    
    if len(file_name.strip()) > 0:

        with open(file_name, "r+") as data:

            for i in data:
            
                if len(i) <= 1:
                    empty_file_alart = input("Empty file. Do you want to update it? yes/no \n")
                    print("\n")
                
                    if empty_file_alart.lower() == "yes" and len(empty_file_alart) > 0:
                        print("\n")
                        update_box = input("Start typing to update file: \n ")
                    
                        # write new content to the file
                        with open(file_name, "a+") as new_write:
                            print(" \n")
                            new_write.write(update_box)
                    

                        # check if file was written successfully
                        with open(file_name, "a+") as update_read:
                        
                            for m in update_read:

                                if len(m) <= 1:
                                    print("\n")
                                    print("file update failed \n")
                                    quit()
                                else: 
                                    print(m, end="")
                                    print("\n")
                                    print(file_name, " updated")

                    elif empty_file_alart.lower() == "no" and len(empty_file_alart) > 0:
                        print("Bye!!!\n")
                        quit()
                    else:
                        print("invalid input. Try again\n")
                        quit()
                        
                else:
                    print(" \n")
                    print(i.strip(), end="")
                    print("\n")
                    print(text_status.format(round(len(i)/4.8), len(i), "2/1/2023"))
    else:
        print("Invalid response \n")

except FileNotFoundError:
    file_create = input("File not found would you like to create it? yes/no: \n")
    if file_create.lower() == "yes" and len(file_create) > 0:
        with open(file_name, "a+") as new_file:
            new_file.write("\t")
            
            # Check if the file was created successfully or not
            if os.path.exists(file_name):
                print(file_name, " created successfully")
            else:
                print("File creation failed !! \n")

    elif file_create.lower() == "no" and len(file_create) > 0:
        print(" Bye !! \n")
    else:
        print("Invalid response try again \n")
        quit()
