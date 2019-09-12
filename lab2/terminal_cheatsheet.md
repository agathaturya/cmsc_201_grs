# (Linux) Terminal Cheatsheet :sparkles:

### Here are some super useful commands that are **really** helpful to know! Let me know if you find/know of any commands I should add

## Which key is the Meta key?
#### Windows: Alt
#### Mac: **Read Me!!**
**all of this is optional, because you can copy and paste directly in Terminal using `cmd + c`, `cmd + v`, etc., and your mouse/cursor. However, the tabs/spacing might (read: will) get wonky if you use `cmd + c`, `cmd + v`, etc. To avoid that, you can set the Option key as your Meta key**
1. Open Terminal
2. Open Terminal Preferences (` cmd + , `)
3. Go to Profiles :arrow_right: Keyboard :arrow_right: check "Use Option as Meta key"

# Commands
`tab`: autocompletes file and directory names  
`cd`: goes to home directory   
`cd ..`: goes up one directory   
`cd directory_name`: move to directory called `directory_name`   
`pwd`: prints file path of current directory   
`ls`: prints contents of current directory]   
`ls -a`: prints **all** contents of directory (**hidden** and unhidden contents)   
`rmdir directory_name`: removes **empty** directory   
`mkdir directory_name`: creates a new, empty directory called directory_name   
`clear`: "clears" the terminal (past commands/content will still be there if you scroll up)   
`cmd + k` (can use on mac, **not windows**): ***actually*** clears the terminal (literally **completely** clears the screen, gets rid of everything printed previously)   
`ctrl + k`: kills (cuts) line after cursor (can paste this line)   
`ctrl + _`: undo   
`ctrl + g`: redo   
`ctrl + space`: highlights a region of text   
`ctrl + w`: kills (cuts) selected region of text   
`Meta + w`: copy   
`ctrl + y`: paste (yank)   
`ctrl + c`: stops whatever you're running   
`up arrow`: select past command   
`cp file_i_want_to_copy new_file_name`: copies `file_i_want_to_copy` into current directory, renames it to `new_file_name`. if you don't want to rename the file, replace `new_file_name` with `.`
