#!/usr/bin/python
# script for automatic Netaccess approval for IIT Madras network
# Author: Cibin Joseph
# Last Updated: 27 Dec 2017
# License: MIT License
 
username="YourUsername"
password="YourPassword"

if (username=="YourUsername"):
    print('** Note: Username and password details can be set permanently in /usr/bin/netaccess.py **')

import getpass

try:
    try:
        import mechanize
        import ssl
    except:
        import sys
        if sys.version_info[0] >= 3:
            print("ERROR: Use Python version < 3 to run code")
        else:
            print("ERROR: mechanize library not found")
            print("Run following commands to install mechanize")
            print("1. sudo apt install pip")
            print("2. sudo pip install mechanize")

    br=mechanize.Browser()

    try:
        ssl._create_default_https_context = ssl._create_unverified_context
        br.set_handle_robots(False)
        response=br.open("https://netaccess.iitm.ac.in/account/login") 
        print('1/3 Page')
    except:
        print("ERROR: Webpage unavailable - check LAN connection and server status")
        exit(1)
    try:
        br.select_form(nr=0)
    except:
        print("ERROR: Webpage unavailable - check LAN connection and server status")
        exit(1)

    if (username=="YourUsername"):
        print("Username has not been set in code. Enter LDAP Username")
        username=raw_input('Username: ')
    if (password=="YourPassword"):
        print("Password has not been set in code. Enter LDAP Password")
        password=getpass.getpass()

    br.form["userLogin"]=username
    br.form["userPassword"]=password
    url1=br.geturl()
    result=br.submit()
    url2=br.geturl()
    if (url1==url2):
        print("ERROR: Wrong username or password")
        exit(1)

    # Second page
    print('2/3 Page')
    br.visit_response(result)

    # Third page
    print('3/3 Page')
    br.follow_link(br.find_link(url_regex="approve"))
    br.select_form(nr=0)
    br.form["duration"] = ["2"]
    result=br.submit()

    print("APPROVAL SUCCESFUL")
except:
    print("APPROVAL UNSUCCESSFULL")
