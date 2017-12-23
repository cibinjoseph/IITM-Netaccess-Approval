#!/usr/bin/python
# script for automatic Netaccess approval for IIT Madras network
# Author: Cibin Joseph
# Last Updated: 23 Dec 2017

try:
    try:
        import mechanize
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
        response=br.open("https://netaccess.iitm.ac.in/account/login") 
        print('1/3 Page')
    except:
        print("ERROR: Webpage unavailable - check LAN connection and server status")
    try:
        br.select_form(nr=0)
    except:
        print("ERROR: Webpage unavailable - check LAN connection and server status")

    br.form["userLogin"]="ae14d214"
    br.form["userPassword"]="^2JcW1@k"
    result=br.submit()

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
