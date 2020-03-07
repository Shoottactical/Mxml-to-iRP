# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#
# braille.py
#
# usage:
#   python3 braille.py <filename>
#
# Reads a MusicXML file specified on the command line,
# converts it to Braille music, and outputs the result to the terminal.
# The output can be redirected to a file or piped directly to a Braille embosser.
#
# There are two different formats for representing Braille electronically - Unicode and ASCII.
# This script can output either, but currently you need to manually configure this
# by commenting and uncommenting lines within the script (see below).
# Would be better to have a command line option to control this!
#


import sys

from music21 import *
from music21.braille import basic
from music21.braille import translate
#
#
name = sys.argv[1]
score = converter.parse(name)
brailleUnicode = translate.objectToBraille(score, debug=False)
#
## Use this to print the Braille to the terminal using Unicode characters.
## this will *look* like Braille, which is nice for sighted folk.
## But it's actually not so useful to other Braille tools, which generally work from ASCII.
#
print(brailleUnicode)
#
## Use this to print the Braille to the terminal using ASCII characters.
## This will look like random garbage - "_>'%^HC_FCW*^HC_EC<_W ;B^G_EI*JDE^2" etc.
## But it can be sent to other tools, such as a Braille embosser that will "print" using dots.
#
brailleAscii = basic.brailleUnicodeToBrailleAscii(brailleUnicode)
print(brailleAscii)
