# Convert PTF to HKF
# Convert a plaintext file like BungeePixel.txt to a javascript mapping in hugs and kisses format

# Plaintext Font Format
# a glyph begins with a new line and a pound sign
# the character represented by the glyph follows the pound sign
# all following lines up to the next pound sign belong to that glyph
# asterisks represent black, spaces represent white, new lines are new lines

# for example:
"""
#a
  *****  
 ******* 
 *** *** 
 *** *** 
 ******* 
 ******* 
 *** *** 
 *** *** 
         
"""

# and here is the same glyph converted to hugs and kisses:
"""
"a": "XXOOOOOXX\nXOOOOOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOOOOOX\nXOOOOOOOX\nXOOOXOOOX\nXOOOXOOOX\nXXXXXXXXX\n",
"""



import string
import os

basePath = os.path.split(os.path.split(__file__)[0])[0]
print '{'
with open(os.path.join(basePath, "BungeePixel.txt")) as pixelFontFile:
    pixelFontLines = pixelFontFile.readlines()
    glyphs = []
    thisGlyph = ''
    thisName = None
    for i, line in enumerate(pixelFontLines):
        if line[0] == '#':
            if i != 0:
                glyphs.append((thisName, thisGlyph))
            thisGlyph = ''
            thisName = string.strip(line[1:])
        else:
            thisGlyph += line.replace(' ', 'X').replace('*', 'O').replace('\n', '\\n')
            
    glyphs.append((thisName, thisGlyph))

    for gname, glyph in glyphs:
        print '\t"%s": "%s",' %(gname, glyph)
print '}'