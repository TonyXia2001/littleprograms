import sys
def main():
    if len(sys.argv) > 2:
        print("what are you talking about...")
        return 1
    elif len(sys.argv) == 1:
        Notenum = int(input("how many notes are there in this chord?"))
    elif len(sys.argv) == 2:
        Notenum = int(sys.argv[1])
    if Notenum != 3 and Notenum != 2:
        print("we currently only support intervals or triads in an octave")



    #it's an interval
    if Notenum == 2:
        firstnote = note(input("what's the bass note?"))
        secondnote = note(input("what's the second note?"))

        if firstnote.name[0] > secondnote.name[0]:
            intnum = ord(secondnote.name[0]) + 8 - ord(firstnote.name[0])
        elif firstnote.name[0] == secondnote.name[0]:
            intnum = 1
        else:
            intnum = ord(secondnote.name[0]) + 1 - ord(firstnote.name[0])

        if firstnote.relpitch > secondnote.relpitch:
            secondnote.addoneoctave()
            semitonediff = secondnote.relpitch - firstnote.relpitch
        else:
            semitonediff = secondnote.relpitch - firstnote.relpitch


        ##checking what chord this is
        #checking if it's a "perfect distance"
        if intnum == 1 or intnum == 4 or intnum == 5:
            if semitonediff == 0 or semitonediff == 5 or semitonediff == 7:
                intqual = "perfect"
            elif semitonediff == 1 or semitonediff == 8:
                intqual = "augmented"
            elif semitonediff == 11 or semitonediff == 4:
                intqual = "diminished"
            elif semitonediff == 6:
                print("the interval is a tritone")
                return 0
            else:
                print("DON'T EVER USE THIS INTERVAL!!!!!!!...")
                return 1
        if intnum == 2:                                     #seconds
            if semitonediff == 0:
                intqual = "diminished"
            elif semitonediff == 1:
                intqual = "minor"
            elif semitonediff == 2:
                intqual = "major"
            elif semitonediff == 3:
                intqual = "augmented"
            else:
                print("DON'T EVER USE THIS INTERVAL!!!!!!!...")
                return 1
        if intnum == 3:                                    #thirds
            if semitonediff ==2:
                intqual = "diminished"
            elif semitonediff == 3:
                intqual = "minor"
            elif semitonediff == 4:
                intqual = "major"
            elif semitonediff == 5:
                intqual = "augmented"
            else:
                print("DON'T EVER USE THIS INTERVAL!!!!!!!...")
                return 1
        if intnum == 6:                                    #sixths
            if semitonediff ==7:
                intqual = "diminished"
            elif semitonediff == 8:
                intqual = "minor"
            elif semitonediff == 9:
                intqual = "major"
            elif semitonediff == 10:
                intqual = "augmented"
            else:
                print("DON'T EVER USE THIS INTERVAL!!!!!!!...")
                return 1
        if intnum == 7:                                    #sevenths
            if semitonediff ==9:
                intqual = "diminished"
            elif semitonediff == 10:
                intqual = "minor"
            elif semitonediff == 11:
                intqual = "major"
            elif semitonediff == 12:
                intqual = "augmented"
            else:
                print("DON'T EVER USE THIS INTERVAL!!!!!!!...")
                return 1

        intnamemaker(intnum, intqual)

    #it's a triad
    if Notenum == 3:
        firstnote = note(input("what's the bass note?"))
        secondnote = note(input("what's the second note?"))
        thirdnote = note(input("what's the highest note?"))



#define a note
class note:
    def __init__(self, name):
        self.name = name.title()
        while not self.checkvalid():
            self.name = input("what's the note again?").title()

        if self.name[0]  == "C":
            self.relpitch = 1
        elif self.name[0] == "D":
            self.relpitch = 3
        elif self.name[0] == "E":
            self.relpitch = 5
        elif self.name[0] == "F":
            self.relpitch = 6
        elif self.name[0] == "G":
            self.relpitch = 8
        elif self.name[0] == "A":
            self.relpitch = 10
        elif self.name[0] == "B":
            self.relpitch = 12

        if len(self.name) == 2:
            if self.name[1] == "#":
                self.relpitch += 1
            else:
                self.relpitch -= 1

        if len(self.name) == 3:
            if self.name[1] == "#":
                self.relpitch += 2
            else:
                self.relpitch -= 2

    def addoneoctave(self):
        self.relpitch += 12

    def checkvalid(self):
        if len(self.name) == 1: #without accidentals
            if not ((self.name >= "A" and self.name <= "G") or (self.name >= "a" and self.name <= "g")):
                return False
            else:
                return True
        if len(self.name) == 2: #with one accidental
            if not ((self.name[0] >= "A" and self.name[0] <= "G") or (self.name[0] >= "a" and self.name[0] <= "g")):
                return False
            else:
                if not (self.name[1] == "b" or self.name[1] == "#"):
                    return False
                else:
                    return True
        if len(self.name) == 3: #double flat or double sharp
            if not ((self.name[0] >= "A" and self.name[0] <= "G") or (self.name[0] >= "a" and self.name[0] <= "g")):
                return False
            else:
                if not (self.name[1] == "b" or self.name[1] == "#"):
                    return False
                else:
                    if not (self.name[2] == self.name[1]):
                        return False
                    else:
                        return True
        else:
            return False

def intnamemaker(intnum, intqual):
    if intnum == 1:
        intdis = "unison"
    elif intnum == 2:
        intdis = "second"
    elif intnum == 3:
        intdis = "third"
    elif intnum == 4:
        intdis = "fourth"
    elif intnum == 5:
        intdis = "fifth"
    elif intnum == 6:
        intdis = "sixth"
    elif intnum == 7:
        intdis = "seventh"

    print("the interval is a " + intqual + " " + intdis)


if __name__ == '__main__':
    main()
