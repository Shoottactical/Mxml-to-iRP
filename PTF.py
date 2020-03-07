# -*- coding: utf-8 -*-
"""
This is a playground file

@author: Lord Pineapple the V
"""

####Important:####
#to get python as an exe use pyinstaller
#pip install pyinstaller
#run: pyinstaller programName.py
#returns programName.exe
#there is a way to add image to exe file
#details at https://pyinstaller.readthedocs.io/en/stable/usage.html

#imports
import music21 as m21
import sys
import webbrowser as web
from os.path import realpath


web.get(using=None) #None = default, others: 'mozilla', 'firefox', 'safari', 'google-chrome', 'chrome', and more
new = 1 #0 is in the window, 1 is a new window, 2 is in a new tab
# Open a public url 
url = "http://docs.python.org/library/webbrowser.html"
web.open(url, new=new)

# to Open a html file locally use
url = "file://" + realpath(README.html) 
web.open(url, new=new)

