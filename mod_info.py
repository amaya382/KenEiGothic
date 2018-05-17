#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import path
import fontforge as ff
import sys

VERSION = 1.1
VERSION_STR = str(VERSION)
FAMILYNAME = sys.argv[1] + sys.argv[3]
FAMILYNAME_JA = sys.argv[2] + sys.argv[3]
WEIGHT = sys.argv[4]
FONTNAME = FAMILYNAME + "-" + WEIGHT
FONTNAME_JA = FAMILYNAME_JA + "-" + WEIGHT
FONT_FILE = FONTNAME + ".ttf"
FONT_PATH = path.join(sys.argv[5], FONT_FILE)

target = ff.open(FONT_PATH)

def generate_copyright(font):
    s = "\n\n"
    s += "* " + font.fontname
    s += "\n"
    s += font.copyright
    return s
copyright = "KenEiGothic is based on the following products:"
copyright += generate_copyright(target)
target.copyright = copyright
target.sfnt_names = \
    tuple((row[0], row[1], copyright if row[1] == "Copyright" else row[2]) \
        for row in target.sfnt_names)

target.fontname = FONTNAME
target.familyname = FAMILYNAME
target.fullname = FONTNAME
target.appendSFNTName("English (US)", "Copyright", copyright)
target.appendSFNTName("English (US)", "Version", VERSION_STR)
target.appendSFNTName("English (US)", "UniqueID", FONTNAME + " " + VERSION_STR)
target.appendSFNTName("English (US)", "Preferred Family", FAMILYNAME)
target.appendSFNTName("English (US)", "Preferred Styles", WEIGHT)
target.appendSFNTName("Japanese", "Family", FONTNAME_JA)
target.appendSFNTName("Japanese", "Fullname", FONTNAME_JA)
target.appendSFNTName("Japanese", "Preferred Family", FAMILYNAME_JA)
target.appendSFNTName("Japanese", "Preferred Styles", WEIGHT)

# Generate
target.generate(FONT_PATH)

