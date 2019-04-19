# Make Your Life Easier
This repository contains shell script files for Unix-based system that automate mundane processes.

## Geting started

### TL;DR: Copy this into your terminal and run it
```
cd && mkdir bin && cd bin && git clone https://github.com/Minter27/make-life-easier.git . && chmod -R u+x .
```

### NOTE: This will guide you through the steps of making a universal script file that can be run from anywhere in Terminal.

- #### Create a bin directory on your user's root. (Users/$whoami)
```
$ cd ~
$ mkdir bin  
```
- ####  Export bin directory to the PATH
##### Open `.bash_profile` (if you're using bash) located on the user's root directory `/Users/$whoami/.bash_profile` in your favorite text editor.
```
$ cd ~
$ open .bash_profile
```
##### Add this to your `.bash_profile` export the directory to `$PATH ` -- User is your username (whoami)
`export PATH=$PATH:/Users/<user>/bin`
- #### Clone the contents of the repo into the bin folder.
##### NOTE: If you don't have git, just the download the zip file and extract its contents into `~/bin`
```
$ cd ~/bin
$ git clone https://github.com/Minter27/make-life-easier.git .
```
- #### Set the correct permission so you can run it from anywhere on the `Terminal`
``` 
$ cd ~/bin
$ chmod -R u+x .
```

## TODO
- [x] ~~Get rid of helpers and migrate functionality into shell script~~
