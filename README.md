# IITM-Netaccess-Approval
Python code that utilizes the mechanize library for netaccess approval of the IIT Madras network from command line

## Usage
1. To run code, use command `netaccess`
2. To avoid having to input username and password every time the code is executed, enter them directly in the code located at `/usr/bin/netaccess.py` in the fields *"YourUsername"* and *"YourPassword"* in line number 7 and 8. Retain the double quotes.
3. Leaving the password field unchanged lets you input it during runtime securely.

## Installation
### Quick Installation
An AUTOINSTALL script is available in this repository that automatically installs all necessary programs with minimal user intervention. Copy the script AUTOINSTALL and run it using sudo priveleges by invoking the command
```sh
sudo bash AUTOINSTALL
```
Further, the code may be run when desired by using the command 
```sh
netaccess
```
To avoid entering username and password everytime on execution, refer the section on Usage above.
All instructions provided below are automatically executed by the script AUTOINSTALL.

### Normal Installation
An INSTALL script is also available for users who would like to install after performing a git clone as described below.

## Getting Started
To get a copy of the project up and running on your local machine for development and testing purposes run
```sh
git clone "git://github.com/cibinjoseph/IITM-Netaccess-Approval.git"
```

## Prerequisites
Ensure the following programs/libraries are installed on your system. If not, use the corresponding commands provided to install them (For Ubuntu OS) 
1. git `sudo apt install git`
2. python `sudo apt install python`
3. pip `sudo apt install python-pip`
4. mechanize library for Python `pip install mechanize`

## Setup
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
