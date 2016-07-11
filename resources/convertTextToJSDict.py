import string
with open(u"/Users/david/Desktop/bungeePixel/bungeePixel.txt") as pixelFontFile:
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
        print '"%s": "%s",' %(gname, glyph)