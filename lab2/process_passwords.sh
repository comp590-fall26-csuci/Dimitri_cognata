#!/bin/bash 

# create a directory to hold the passwords
mkdir -p password_files 

#start teh count numbering the files at 1
count=1

# sort the passwords alphabetically and loop through each 
for password in $(sort passwords.txt)
do 
    #print out the password to the terminal
    echo "$password"
    #save each password to its own numbered file
    echo "$password" > password_files/password$count.txt 
    
    # continue to the next password by increasing the file number by 1
    count=$((count + 1))

done    
