# Libraries
import music21

# Constants
message = "i love codeland!"

# Mappings
mappingsDictionary = {  #letter : pitch
                        "i" : "A3",
                        "l" : "B3",
                        "o" : "C4",
                        "v" : "D4",
                        "e" : "E4",
                        "c" : "F4",
                        "d" : "G4",
                        "a" : "G#4",
                        "n" : "A4"
}

# Music constants
harp = music21.instrument.Harp() # instrument
noteLengths = 1                  # note length

# ---- Process Text
characterList = list(message) # Break text into characters

#---- MUSICAL TRANSLATION
#-- Set up musical piece
s = music21.stream.Stream() # create stream for entire piece
p = music21.stream.Part()   # add instrument part to music
p.insert(0, harp)           # choose instrument playing

#-- Add notes, character by character in characterList
for character in characterList:

    # Is the character in mappingsDictionary
    if character in list(mappingsDictionary.keys()):
        # Yes, get pitch, define note
        pitch = mappingsDictionary[character]
        nextNote = music21.note.Note(
                    pitchName = pitch,
                    quarterLength = noteLengths)

    else:
        # No, define the rest
        nextNote = music21.note.Rest(
                    quarterLength = noteLengths)

    # add the next note to harp part
    p.append(nextNote)

s.append(p)     # add part to stream

# --- Save File
s.write('midi', fp = "iLoveCodeland.mid")
