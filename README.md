# Linux Brightness Controller

Linux Brightness Controller allows you to control Brightness of your **Display** with the help of `xrandr` and `xbacklight` in Linux. It's a RandR-based Linux control application. The controller is created using Python, which in the back end calls `os.system` to execute system commands.


## Dependencies

Three dependencies only.

1. **Python** - Linux should have it by default

2. **Python WxWidgets**
```bash
$ sudo apt-get install python-wxgtk2.8
```
3. **`xrandr` and `xbackLinux`** - that's what the program uses in the backend to control the brightness of your monitor!

## Installation 

There are mainly two options available. One is for users, involving installers designed for your distro, or a bash script based installer for all platforms. The other is for developers, involving a git clone based script.

1. **$sudo apt-get install xrandr xbacklight**

2. **$sudo apt-get install python python-wxgtk2.8**

3. Finally run the source file
	**$python LinuxBrightnessController.py**

## FAQ

Random questions that might show up here are answered here in advance.

### Why is it here?

I wrote it because I could not find any other similar software available in **Linux** that provides an easy to use UI for changing brightness. There are still room for improvement, specially in the coding style. I hope due to its open source nature, people will come forward and will help it become a better Brightness Controller.

## Screenshots

Apperance is subject to change based on the theme you are using. These screenshots were taken in Linux Mint environment.

![Screenshot 1](https://raw.github.com/asifhj/Linux-Brightness-Controller/master/img/shot1.png)

![Screenshot 2](https://raw.github.com/asifhj/Linux-Brightness-Controller/master/img/shot2.png)

>>>>>>> Initial commit
