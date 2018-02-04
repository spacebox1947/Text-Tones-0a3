class FileLoader(object):
    """
    # FileLoader grabs a text file and parses each line as strings.
    # Boom.
    # would be nice if it could fetch the current project dir.
    """
    def __init__(self, filcode, name, sanitize):
        self.filcode = filcode
        self.file = None
        self.data = []
        self.name = name
        self.readType = 'r'
        self.sanitize = sanitize
        self.breaks = []

    def setFilcode(self, fileStr):
        self.filcode = fileStr

    def setName(self, newName):
        self.name = newName

    def getFilcode(self):
        return self.filcode

    def genFileArray(self):
        print("Opening {}...\nLoading into an array!".format(self.filcode))
        print("Sanitization of \\r\\n == {}".format(self.sanitize))
        self.file = open(self.filcode, self.readType)
        if self.sanitize:
            count = 0
            for lines in self.file:
                if len(lines) >= 3:
                    #self.data.append(lines[:-1])
                    self.data.append(lines)
                    count += 1
                else:
                    if count-1 not in self.breaks:
                        self.breaks.append(count-1)
        else:
            for lines in self.file:
                #self.data.append(lines[:-1])
                self.data.append(lines)
        self.file.close()
        print("Loaded into {}. Success!".format(self.name))
        print("The file has {} lines.".format(self.getLength()))
        if self.sanitize:
            print("There are {} breaks in this file.".format(len(self.breaks)))

    def getLine(self, n):
        return self.data[n]

    def getFileArray(self):
        return self.data

    def getBreaks(self):
        return self.breaks

    def getBreakByIndex(self, idx):
        return self.breaks[idx]

    def getLength(self):
        return len(self.data)

    def getName(self):
        return self.name

    def getSanitize(self):
        return self.sanitize

    def printToConsole(self):
        print ("\n---- PRINTING TO CONSOLE! ----\n")
        bz = 0
        for lines in range(len(self.data)):
            if lines == self.breaks[bz]:
                print ("[{}]::>{}".format(lines, self.data[lines]))
                print ("\t\\n\\r @ {}".format(self.breaks[bz]))
                if bz+1 < len(self.breaks):
                    bz+=1
            else:
                print ("[{}]::>{}".format(lines, self.data[lines]))
        print ("\n---- DAMN, I\'M BEAUTIFUL! ----\n")
            
