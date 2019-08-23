# Make Your Life Easier
This repository contains shell script files for Unix-based system that automate mundane processes.

## Demos
### android-emulator (outdated)
![android-emulator-gif](https://media.giphy.com/media/XF4Zl84i5bKAfx1Zor/giphy.gif)

## Geting started

### TL;DR: Copy this into your terminal and run it
```
mkdir ~/bin && echo "export PATH=$PATH:/Users/$USER/bin" >> ~/.bash_profile && source ~/.bash_profile && cd bin && git clone https://github.com/mohshbool/make-life-easier.git . && chmod -R u+x .
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
##### Add this to your `.bash_profile` export the directory to `$PATH`.
`export PATH=$PATH:/Users/$USER/bin`
- #### Clone the contents of the repo into the bin folder.
##### NOTE: If you don't have git, just the download the zip file and extract its contents into `~/bin`
```
$ cd ~/bin
$ git clone https://github.com/mohshbool/make-life-easier.git .
```
- #### Set the correct permission so you can run it from anywhere on the `Terminal`
``` 
$ cd ~/bin
$ chmod -R u+x .
```

## Scipt-specific Information

### commit
- #### Requires `git` to be installed.

### android-emulator
#### Usage:
- `$ android-emulator` to show available devices and then prompt you to enter the desired device to launch.
- `$ android-emulator show` to show available devices.
- `$ android-emulator run <device_name>` to run a specific device.

### mongoexportdb
- #### Requires `mongo-cli` to be installed.


## TODO
- [x] ~~Get rid of helpers and migrate functionality into shell script~~
- [x] ~~Make device selection by number for ease of use on android-emulator~~
