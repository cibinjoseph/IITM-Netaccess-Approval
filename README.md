# IITM-Netaccess-Approval
Python code that utilizes the mechanize library for netaccess approval of the IIT Madras network from command line

## Quick Installation
An AUTOINSTALL script is available in this repository that automatically installs all necessary programs without user intervention. Copy the script AUTOINSTALL and run it using sudo priveleges by invoking the command
```sh
sudo bash AUTOINSTALL
```
Further, the code may be run when desired by using the command 
```sh
netaccess
```
To avoid entering username and password everytime on execution, refer the section on customizations below.
All instructions provided below are automatically executed by the script AUTOINSTALL.

## Normal Installation
An INSTALL script is also available for users who would like to install after performing a git clone as described below.

# Getting Started
To get a copy of the project up and running on your local machine for development and testing purposes run
```sh
git clone "git://github.com/cibinjoseph/IITM-Netaccess-Approval.git"
```

# Prerequisites
Ensure the following programs/libraries are installed on your system. If not, use the corresponding commands provided to install them (For Ubuntu OS) 
1. git `sudo apt install git`
2. python `sudo apt install python`
3. pip `sudo apt install python-pip`
4. mechanize library for Python `pip install mechanize`

## Customizations
The script *netaccess.py* is by default placed in the directory /usr/bin and may be edited using an editor of your choice (like gedit or vim).
To avoid having to enter username and password every time the code is executed, enter your username and password inside the code in the fields *"YourUsername"* and *"YourPassword"* in line number 7 and 8. Retain the double quotes. Leaving the password field unchanged lets you input your password during runtime securely.

## Usage
After installation, change the mode of the code to 'executable' by issuing the command
```sh
sudo chmod +x netaccess.py
```

Move the code to /usr/bin for universal access. The code may then be run by issuing
```sh
netaccess
```

## Author
[**Cibin joseph**](https://github.com/cibinjoseph/), Aerospace Engineering, IIT Madras

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
