def main():
    #take an input
    toParse = sequence()
    print("Please type in your note sequence with notes separated by spaces:")
    inputbuffer = input()
    toParse.setNotes(inputbuffer.split(" "))
    if not toParse.checkvalid():
        print("your sequence is invalid!")
        return 1
    print("the sequence is in " + toParse.parsekey())



class sequence:
    #todo
    def __init__(self):
        self.notes = []
        self.accidentalnum = 0
        self.accidentals = []
        self.majsharpkeysignature = ["F#", "C#", "G#", "D#", "A#", "E#", "B#"]
        self.majflatkeysignature = ["Bb", "Eb", "Ab", "Db", "Gb", "Cb", "Fb"]
        self.majkey = ["Cb", "Gb", "Db", "Ab", "Eb", "Bb", "F", "C", "G", "D", "A", "E", "B", "F#", "C#"]
        self.key = ""

    def parsekey(self):
        #todo
        self.accidentalnum = self.countingaccidentals()
        if self.accidentalnum == 0:
            self.key = "C Major"
            return self.key
        foundsharpmajor = True
        foundflatmajor = True
        for i in range(self.accidentalnum):
            if not self.majsharpkeysignature[i] in self.accidentals:
                foundsharpmajor = False
            if not self.majflatkeysignature[i] in self.accidentals:
                foundflatmajor = False
        if foundflatmajor:
            self.key = self.majkey[7 - self.accidentalnum] + " Major"
        elif foundsharpmajor:
            self.key = self.majkey[7 + self.accidentalnum] + " Major"
        else:
            self.key = "not yet able to parse the chord..."
        return self.key


    def setNotes(self, listofnotes):                            #set the notes
        self.notes = listofnotes                                #in the sequence
        for i in range(len(self.notes)):
            self.notes[i] = self.notes[i].title()


    def checkvalid(self):                                       #check if the
        validity = True                                         #notes are valid
        for note in self.notes:
            namelength = len(note)
            if namelength >= 4 or namelength <=0:
                validity = False
            else:
                if note[0] >= "A" and note[0] <= "Z":
                    if namelength == 1:
                        continue
                    elif namelength == 2:
                        if note[1] != "#" and note[1] != "b":
                            validity = False
                        else:
                            continue
                    elif namelength == 3:
                        if (note[1] == "#" or note[1] == "b") and note[1] == note[2]:
                            continue
                        else:
                            validity = False
        return validity



    #return the number of acccidentals
    def countingaccidentals(self):
        counter = 0
        for note in self.notes:
            if len(note) >=2:
                if not note in self.accidentals:
                    self.accidentals.append(note)
                    counter += 1
                else:
                    continue
            else:
                continue
        return counter


if __name__ == '__main__':
    main()
