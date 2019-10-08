# Symbolic Links

## What is a symbolic link?
A **symbolic link** is a _pointer_ (a.k.a. a shortcut, alias, etc) to a **location** in a linux file system. A location can be a file **_or_** a directory. This picture is also a pretty good explanation.
![Symbolic Link](phonto.PNG)

## Why use them?
Make your life _so_ much easier when typing in long directory names. If I create a symbolic link to my directory `/afs/umbc.edu/users/a/g/agatha3/pub/201_grs` and name it `grs_activities`, I no longer have to type in the whole entire directory name; I can just use my symbolic link `grs_activities` instead.

## Creating a symbolic link to my 201 GRS Directory
1. Run this command in your home directory:  
`ln -s /afs/umbc.edu/users/a/g/agatha3/pub/201_grs grs_activities`. This symbolic link is named `grs_activities`.
2. To ensure your symbolic link was created successfully, `ls` in your home directory. `grs_activities` should show up.

## Using symbolic links
Symbolic links are used in the **same way** as a regular directory or file. For example, if I wanted to get the file named `activity.py` from the `/afs/umbc.edu/users/a/g/agatha3/pub/201_grs/example/activity.py` directory, I can use my symbolic link. To copy the file, I would run this command: `cp grs_activities/example/activity.py .`. This command is identical to using this command without a symbolic link: `cp /afs/umbc.edu/users/a/g/agatha3/pub/201_grs/example/activity.py .`

## Notes
[More in-depth explication](https://linuxize.com/post/how-to-create-symbolic-links-in-linux-using-the-ln-command/)
