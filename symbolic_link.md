# Symbolic Links
## What is a symbolic link?
A **symbolic link** is a pointer (aka a shortcut, alias, etc) to a directory

## Why use them?
Make your life _so_ much easier when typing in long directory names

## Creating a symbolic link to my 201 GRS Directory
1. Run this command in your home directory:  `ln -s /afs/umbc.edu/users/a/g/agatha3/pub/201_grs grs_activities`. This symbolic link is named `grs_activities`.
2. To ensure your symbolic link was created successfully, `ls` in your home directory. `grs_activities` should show up.

## Using symbolic links
Using symbolic links is the **same** as using a regular directory. For example, if I wanted to get the file named `activity.py` from the `/afs/umbc.edu/users/a/g/agatha3/pub/201_grs/example/activity.py` directory, I can use my symbolic link. To copy the file, I would run this command: `cp grs_activities/example/activity.py .`. This command is identical to using this command without a symbolic link: `cp /afs/umbc.edu/users/a/g/agatha3/pub/201_grs/example/activity.py .`
