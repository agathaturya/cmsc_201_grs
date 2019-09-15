# (Linux) Terminal Cheatsheet :sparkles:

### Here are some super useful commands that are **really** helpful to know! Let me know if you find/know of any commands I should add

## Which key is the Meta key?
#### Windows: Alt
#### Mac: **Read Me!!**
**setting up a Meta key is optional, because you can copy and paste directly in Terminal using `cmd + c`, `cmd + v`, etc., with your mouse/cursor. However, the tabs/spacing might (read: will) get wonky if you use `cmd + c`, `cmd + v`, etc. To avoid that, you can set the Option key as your Meta key**
1. Open Terminal
2. Open Terminal Preferences (` cmd + , `)
3. Go to Profiles :arrow_right: Keyboard :arrow_right: check "Use Option as Meta key"

# Commands

## Navigating through directories
`tab`: autocompletes file and directory names  
`cd`: goes to home directory   
`cd ..`: goes up one directory   
`cd directory_name`: move to directory called `directory_name`
`pwd`: prints file path of current directory 
`ls`: prints contents of current directory]   
`ls -a`: prints **all** contents of directory (**hidden** and unhidden contents) 

## Modifying directories
`rmdir directory_name`: removes **empty** directory   
`mkdir directory_name`: creates a new, empty directory called directory_name 
`mv directory_to_be_moved destination_directory`: moves `directory_to_be_moved` to `destination_directory`

## "Shortcuts" and misc.
`clear`: "clears" the terminal (past commands/content will still be there if you scroll up)  
`tab`: autocompletes file and directory names  
`up arrow`: select past command  
`cmd + k` (can use on mac, **not windows**): ***actually*** clears the terminal (literally **completely** clears the screen, gets rid of everything printed previously, gets rid of all past commands)  
`ctrl + c`: stops whatever you're running  
`whoami`: prints current user

## Copying, cutting, and pasting
`ctrl + k`: kills (cuts) line after cursor (can paste this line)   
`ctrl + _`: undo   
`ctrl + g`: redo   
`ctrl + space`: highlights a region of text   
`ctrl + w`: kills (cuts) selected region of text   
`Meta + w`: copy   
`ctrl + y`: paste (yank)   

## Modifying and creating files
`cp file_i_want_to_copy new_file_name`: copies `file_i_want_to_copy` into current directory, renames it to `new_file_name`. if you don't want to rename the file, replace `new_file_name` with `.`  
`curl -O "my-file-url.com/file_name.txt"`: downloads file from given URL into current directory, filename remains the same  
`touch my_file`: creates an empty file called my_file in current directory. note: remember to put appropriate file ending  
`emacs my_file`: opens a file called my_file. if my_file doesn't exist, it creates an empty file and opens it in emacs. if you **_don't_** edit an empty file that was created via the `emacs` command, **the (empty) file will be deleted!!!**. note: remember to put appropriate file ending  
`mv file_to_be_moved destination`: moves `directory_to_be_moved` to `destination`. **note**: `destination` can be a **file** *or* **directory**. note: remember to put appropriate file ending   
`ctrl + x` `ctrl + c`: save and exit emacs file  
`ctrl + x`: save emacs file  
`ctrl + c`: exit emacs file **without saving**. you may have to press `y` or type `yes` to "force exit" . 

## Vim
### note: do _**not**_ use vim unless you know how to use vim
`:w`: save
`:wq` or `:x`: save and exit

