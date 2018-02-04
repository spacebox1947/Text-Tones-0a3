class DocumentParameters(object):
    """
    #
    # Holds the values for creating a document
    #
    """
    def __init__(self):
        """
        # pt and ptMusic (font sizes) are defined separately.
        #
        # Eat it.
        """
        self.pt = 18
        self.ptMusic = 19
        self.ptLineSpacing = 1.5
        self.fontName = 'Lucida Console'
        self.tab = True

    def repr(self):
        print("Font: {}\tSize(Pt): {}\tMSize(Pt): {}".format(self.fontName, self.pt, self.ptMusic))
        print("Line Spacing(Pt): {}\tTab @ |P Start: {}".format(self.ptLineSpacing, self.tab))

    def getPt(self):
        return self.pt

    def getMusicPt(self):
        return self.ptMusic

    def getLineSpacing(self):
        return self.ptLineSpacing

    def getTab(self):
        return self.tab

    def getFontName(self):
        return self.fontName

    def setPt(self, newPt):
        self.pt = newPt

    def setMusicPt(self, newPt):
        self.musicPt = newPt

    def setLineSpacing(self, newLS):
        self.ptLineSpacing = newLS

    def setTab(self, tabBool):
        self.tab = tabBool

    def setFontName(self, newFontName):
        self.fontName = newFontName

    def documentParamsFromList(self, paramList):
        """
        # paramList = [pt, musicPt, lineSpacing, tab, 'Font Name']
        """
        self.pt = paramList[0]
        self.ptMusic = paramList[1]
        self.ptLineSpacing = paramList[2]
        self.tab = paramList[3]
        self.fontName = paramList[4]
