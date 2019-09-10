# GL Cheatsheet :sparkles: :sparkles: :sparkles:

## How to login to GL

### Using a Mac (or any Linux machine)
1. Open the Terminal (I use Spotlight Search because it's super quick: `cmd + space`, then search for Terminal)
2. Use this command: `ssh username@gl.umbc.edu` hint: username is your UMBC username (mine is agatha3). After the command has ran successfully, you'll see this message:  
`WARNING: UNAUTHORIZED ACCESS to this computer is in violation of Criminal Law
         Article section 8-606 and 7-302 of the Annotated Code of MD.

NOTICE:  This system is for the use of authorized users only. Individuals using
         this computer system without authority, or in excess of their authority
         , are subject to having all of their activities on this system
         monitored and recorded by system personnel.`  
3. It will prompt you for your password, enter it. Even though it won't indicate that you're typing, it's getting your input
4. Once you're logged in successfully, you should see something like this: `[username@linux1 ~]`


### Using Windows
1. Download PuTTy using these instructions (from Lab 1). Go to: https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html and scroll
down to “Alternative binary files”. Under “putty.exe (the SSH and Telnet client
itself)”, click on the “64-bit: putty.exe” link to download the “putty.exe” file to your
computer. Make sure to choose a location that you will remember
2. Open the `putty.exe` file to install it
3. Once PuTTy is installed, type `gl.umbc.edu` into the Hostname text field
4. It will prompt you for your username, type in your UMBC username and ***nothing else***. For example, my username is agatha3, so I would type in agatha3.
5. It will prompt you for your password, enter it. Even though it won't indicate that you're typing, it's getting your input.
6. Once you're logged in successfully, you should see something like this: `[username@linux1 ~]`

## Troubleshooting
1. Check that you're connected to internet
2. GL might be down or super slow (happens a lot when a bunch of people are on GL at the same time)
3. Username might be incorrect
4. Password might be incorrect
5. Using incorrect ssh login syntax (should be `ssh username@gl.umbc.edu` on Mac/linux, hostname should be `gl.umbc.edu` on windows)
