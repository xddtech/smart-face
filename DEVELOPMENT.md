
# Check OS
https://stackoverflow.com/questions/8683895/how-do-i-determine-the-current-operating-system-with-node-js
The variable to use would be process.platform
On Mac the variable returns darwin. On Windows, it returns win32 (even on 64 bit).
Current possible values are:
    aix
    darwin
    freebsd
    linux
    openbsd
    sunos
    win32

var isWin = process.platform === "win32";




# nodemon
Monitor for any changes in your node.js application and automatically restart the server - perfect for development

To use nodemon:

$ npm install nodemon -g
$ nodemon main.js


# Troubleshooting a Port Already in Use

    >Stop the conflicting application as follows:
    a. Open the command prompt and enter netstat -aon | findstr "8080". ...
    b. End the conflicting process:
    i. Open Windows Task Manager.
    ii. In the Processes tab, click View > Select Columns.
    iii. Choose PID and click OK.