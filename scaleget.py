import random
import sys

modes = {
    "wwhwwwh" : "Ionian (Major)",
    "whwwwhw" : "Dorian",
    "hwwwhww" : "Phyrgian",
    "wwwhwwh" : "Lydian",
    "wwhwwhw" : "Mixolydian",
    "whwwhww" : "Aeolian (Minor)",
    "hwwhwww" : "Locrian"
        }


harmonic_minor_modes = {"whwwhth":"Harmonic minor" #................





}

melodic_minor_modes = { "whwwwwh":"Melodic minor",
            "hwwwwhw":"Phrygian ♯6 or Dorian ♭2",
            "wwwwhwh":"Lydian Augmented",
            "wwwhwhw":"Lydian Dominant",
            "wwhwhww":"Mixolydian ♭6",
            "whwhwww":"Half-Diminished",
            "hwhwwww":"Altered Dominant"
}




others = {
    "wwwwww":"whole tone (did i really need to tell you this?)",
    "whwhwhwh":"whole half diminished",
    "hwhwhwhw":"half whole diminished",
    "twhhtw": "blues" #....................
}
#E B F#
notes = ["A","A#","Bb","B","C","C#","Db","D","D#","Eb","E","F","F#","Gb","G","G#","Ab"
,"a","a#","bb","b","c","c#","db","d","d#","eb","e","f","f#","gb","g","g#","ab"]

import sys

C_Ionian = ["C Ionian ","C","D","E","F","G","A","B"]
D_Dorian = ["D Dorian "] + C_Ionian[2:] + C_Ionian[1:2]
E_Phrygian = ["E Phrygian "] + C_Ionian[3:] + C_Ionian[1:3]
F_Lydian = ["F Lydian "] + C_Ionian[4:] + C_Ionian[1:4]
G_Mixolydian = ["G Mixolydian "] + C_Ionian[5:] + C_Ionian[1:5]
A_Aeolian = ["A Aeolian "] + C_Ionian[6:] + C_Ionian[1:6]
B_Locrian = ["B Locrian "] + C_Ionian[7:] + C_Ionian[1:7]


Db_Ionian = ["Db Ionian ","C#","D#","F","F#","G#","A#"]
Eb_Dorian = ["Eb Dorian "] + Db_Ionian[2:] + Db_Ionian[1:2]
F_Phrygian = ["F Phrygian "] + Db_Ionian[3:] + Db_Ionian[1:3]
Gb_Lydian = ["Gb Lydian "] + Db_Ionian[4:] + Db_Ionian[1:4]
Ab_Mixolydian = ["Ab Mixolydian "] + Db_Ionian[5:] + Db_Ionian[1:5]
Bb_Aeolian = ["Bb Aeolian "] + Db_Ionian[6:] + Db_Ionian[1:6]
C_Locrian = ["C Locrian "] + Db_Ionian[7:] + Db_Ionian[1:7]


D_Ionian = ["D Ionian ", "D","E","F#","G","A","B","C#"]
E_Dorian = ["E Dorian "] + D_Ionian[2:] + D_Ionian[1:2]
Gb_Phrygian = ["Gb Phrygian "] + D_Ionian[3:] + D_Ionian[1:3]
G_Lydian = ["G Lydian "] + D_Ionian[4:] + D_Ionian[1:4]
A_Mixolydian = ["A Mixolydian "] + D_Ionian[5:] + D_Ionian[1:5]
B_Aeolian = ["B Aeolian "] + D_Ionian[6:] + D_Ionian[1:6]
Db_Locrian = ["Db Locrian "] + D_Ionian[7:] + D_Ionian[1:7]


Eb_Ionian = ["Eb Ionian ","D#","F","G","G#","A#","C","D"]
F_Dorian = ["F Dorian "] + Eb_Ionian[2:] + Eb_Ionian[1:2]
G_Phrygian = ["G Phrygian "] + Eb_Ionian[3:] + Eb_Ionian[1:3]
Ab_Lydian = ["Ab Lydian "] + Eb_Ionian[4:] + Eb_Ionian[1:4]
Bb_Mixolydian = ["Bb Mixolydian "] + Eb_Ionian[5:] + Eb_Ionian[1:5]
C_Aeolian = ["C Aeolian "] + Eb_Ionian[6:] + Eb_Ionian[1:6]
D_Locrian = ["D Locrian "] + Eb_Ionian[7:] + Eb_Ionian[1:7]


E_Ionian = ["E","F#","G#","A","B","C#","D#"]
Gb_Dorian = ["Gb Dorian "] + Eb_Ionian[2:] + Eb_Ionian[1:2]
Ab_Phrygian = ["Ab Phrygian "] + Eb_Ionian[3:] + Eb_Ionian[1:3]
A_Lydian = ["Ab Lydian "] + Eb_Ionian[4:] + Eb_Ionian[1:4]
B_Mixolydian = ["B Mixolydian "] + Eb_Ionian[5:] + Eb_Ionian[1:5]
Db_Aeolian = ["Db Aeolian "] + Eb_Ionian[6:] + Eb_Ionian[1:6]
Eb_Locrian = ["Eb Locrian "] + Eb_Ionian[7:] + Eb_Ionian[1:7]


F_Ionian = ["F Ionian", "F","G","A","A#","C","D","E"]
G_Dorian = ["G Dorian "] + F_Ionian[2:] + F_Ionian[1:2]
A_Phrygian = ["A Phrygian "] + F_Ionian[3:] + F_Ionian[1:3]
Bb_Lydian = ["Bb Lydian "] + F_Ionian[4:] + F_Ionian[1:4]
C_Mixolydian = ["C Mixolydian "] + F_Ionian[5:] + F_Ionian[1:5]
D_Aeolian = ["D Aeolian "] + F_Ionian[6:] + F_Ionian[1:6]
E_Locrian = ["E Locrian "] + F_Ionian[7:] + F_Ionian[1:7]


Gb_Ionian = ["Gb Ionian ","F#","G#","A#","B","C#","D#","F"]
Ab_Dorian = ["Ab Dorian "] + Gb_Ionian[2:] + Gb_Ionian[1:2]
Bb_Phrygian = ["Bb Phrygian "] + Gb_Ionian[3:] + Gb_Ionian[1:3]
B_Lydian = ["B Lydian "] + Gb_Ionian[4:] + Gb_Ionian[1:4]
Db_Mixolydian = ["Db Mixolydian "] + Gb_Ionian[5:] + Gb_Ionian[1:5]
Eb_Aeolian = ["Eb Aeolian "] + Gb_Ionian[6:] + Gb_Ionian[1:6]
F_Locrian = ["F Locrian "] + Gb_Ionian[7:] + Gb_Ionian[1:7]


G_Ionian = ["G Ionian ", "G","A","B","C","D","E","F#"]
A_Dorian = ["A Dorian "] + G_Ionian[2:] + G_Ionian[1:2]
B_Phrygian = ["B Phrygian "] + G_Ionian[3:] + G_Ionian[1:3]
C_Lydian = ["C Lydian "] + G_Ionian[4:] + G_Ionian[1:4]
D_Mixolydian = ["D Mixolydian "] + G_Ionian[5:] + G_Ionian[1:5]
E_Aeolian = ["E Aeolian "] + G_Ionian[6:] + G_Ionian[1:6]
Gb_Locrian = ["Gb Locrian "] + G_Ionian[7:] + G_Ionian[1:7]


Ab_Ionian = ["Ab Ionian ", "G#","A#","C","C#","D#","F","G"]
Bb_Dorian = ["Bb Dorian "] + Ab_Ionian[2:] + Ab_Ionian[1:2]
C_Phrygian = ["C Phrygian "] + Ab_Ionian[3:] + Ab_Ionian[1:3]
Db_Lydian = ["Db Lydian "] + Ab_Ionian[4:] + Ab_Ionian[1:4]
Eb_Mixolydian = ["Eb Mixolydian "] + Ab_Ionian[5:] + Ab_Ionian[1:5]
F_Aeolian = ["F Aeolian "] + Ab_Ionian[6:] + Ab_Ionian[1:6]
G_Locrian = ["G Locrian "] + Ab_Ionian[7:] + Ab_Ionian[1:7]


A_Ionian = ["A Ionian ", "A","B","C#","D","E","F#","G#"]
B_Dorian = ["B Dorian "] + A_Ionian[2:] + A_Ionian[1:2]
Db_Phrygian = ["Db Phrygian "] + A_Ionian[3:] + A_Ionian[1:3]
D_Lydian = ["D Lydian "] + A_Ionian[4:] + A_Ionian[1:4]
E_Mixolydian = ["E Mixolydian "] + A_Ionian[5:] + A_Ionian[1:5]
Gb_Aeolian = ["Gb Aeolian "] + A_Ionian[6:] + A_Ionian[1:6]
Ab_Locrian = ["Ab Locrian "] + A_Ionian[7:] + A_Ionian[1:7]


Bb_Ionian = ["Bb Ionian", "A#","C","D","D#","F","G","A"]
C_Dorian = ["C Dorian "] + Bb_Ionian[2:] + Bb_Ionian[1:2]
D_Phrygian = ["D Phrygian "] + Bb_Ionian[3:] + Bb_Ionian[1:3]
Eb_Lydian = ["Eb Lydian "] + Bb_Ionian[4:] + Bb_Ionian[1:4]
F_Mixolydian = ["F Mixolydian "] + Bb_Ionian[5:] + Bb_Ionian[1:5]
G_Aeolian = ["G Aeolian "] + Bb_Ionian[6:] + Bb_Ionian[1:6]
A_Locrian = ["A Locrian "] + Bb_Ionian[7:] + Bb_Ionian[1:7]


B_Ionian = ["B Ionian", "B","C#","D#","E","F#","G#","A#"]
Db_Dorian = ["Db Dorian "] + B_Ionian[2:] + B_Ionian[1:2]
Eb_Phrygian = ["Eb Phrygian "] + B_Ionian[3:] + B_Ionian[1:3]
E_Lydian = ["Eb Lydian "] + B_Ionian[4:] + B_Ionian[1:4]
Gb_Mixolydian = ["Gb Mixolydian "] + B_Ionian[5:] + B_Ionian[1:5]
Ab_Aeolian = ["Ab Aeolian "] + B_Ionian[6:] + B_Ionian[1:6]
Bb_Locrian = ["Bb Locrian "] + B_Ionian[7:] + B_Ionian[1:7]


scales = [
C_Ionian,
D_Dorian,
E_Phrygian,
F_Lydian,
G_Mixolydian,
A_Aeolian,
B_Locrian,

Db_Ionian,
Eb_Dorian,
F_Phrygian,
Gb_Lydian,
Ab_Mixolydian,
Bb_Aeolian,
C_Locrian,

D_Ionian,
E_Dorian,
Gb_Phrygian,
G_Lydian,
A_Mixolydian,
B_Aeolian,
Db_Locrian,

Eb_Ionian,
F_Dorian,
G_Phrygian,
Ab_Lydian,
Bb_Mixolydian,
C_Aeolian,
D_Locrian,

F_Ionian,
G_Dorian,
A_Phrygian,
Bb_Lydian,
C_Mixolydian,
D_Aeolian,
E_Locrian,

Gb_Ionian,
Ab_Dorian,
Bb_Phrygian,
B_Lydian,
Db_Mixolydian,
Eb_Aeolian,
F_Locrian,


G_Ionian,
A_Dorian,
B_Phrygian, 
C_Lydian,
D_Mixolydian,
E_Aeolian,
Gb_Locrian,


Ab_Ionian,
Bb_Dorian,
C_Phrygian,
Db_Lydian,
Eb_Mixolydian,
F_Aeolian,
G_Locrian,


A_Ionian,
B_Dorian,
Db_Phrygian, 
D_Lydian,
E_Mixolydian,
Gb_Aeolian,
Ab_Locrian,


Bb_Ionian,
C_Dorian,
D_Phrygian,
Eb_Lydian,
F_Mixolydian,
G_Aeolian,
A_Locrian, 


B_Ionian,
Db_Dorian,
Eb_Phrygian,
E_Lydian, 
Gb_Mixolydian,
Ab_Aeolian, 
Bb_Locrian
]

#C_Harmonicminor  = 
#Db_Harmonicminor  = 
#D_Harmonicminor = 
#E_Harmonicminor=
#Eb_Harmonicminor=
#F_Harmonicminor =
#Gb_Harmonicminor =
#G_Harmonicminor =
#Ab_Harmonicminor =
#A_Harmonicminor = 
#Bb_Harmonicminor =
#B_Harmonicminor =

#C_Melodicminor  = 
#Db_Melodicminor  = 
#D_Melodicminor = 
#E_Melodicminor=
#Eb_Melodicminor=
#F_Melodicminor =
#Gb_Melodicminor =
#G_Melodicminor =
#Ab_Melodicminor =
#A_Melodicminor = 
#Bb_Melodicminor =
#B_Melodicminor =


#be able to go back to menu from prog1/2

import sys

while True:
    print('\n' + '1 : root-interval scale namer' + '\n' + '2 : scale suggester' + '\n' + '3 : random scale' + '\n' + 'e to exit' + '\n')
    s = input()

    if s == 'e':
        break

    elif int(s) == 1: #SCALE DETECTOR PROGRAM

        print("Enter root note followed by sequence of h/w (steps) or minor 3rds (t), e.g. C wwhwwwh or C whwwhth  Enter e for menu")

        while True:

            s = sys.stdin.readline().strip()

            if s == "e":   #exit program
                #print("broke")
                print("\n")
                break


            if s.split(" ")[0] in notes:    #see if valid note

    

                if len(s.split(" ")) == 2:
                    s = s.split(" ") #possibly correct input, read input and split up root and steps

                    root = s[0]
                    steps = s[1]
                    #x = 0
                    #y = 0

                    if steps in modes:
                        print('\n' + root, modes[steps] + '\n' #+ '\n' 
                    # + x + "th mode of " + y)
                            )

                    elif steps in harmonic_minor_modes:
                        print('\n' + root, harmonic_minor_modes[steps] + '\n')

                    elif steps in melodic_minor_modes:
                        print('\n' + root, melodic_minor_modes[steps] + '\n')

                    elif steps in others:
                        print('\n' + root, others[steps] + '\n')
                    else:
                        print("unknown scale")

        #elif

        #elif

        #else:
            #break  #user input unrecognized, breaks elif len(s.split() == 2):, which brings us to else below, which starts the while true loop over

                else:
                    print("Please enter a root followed by a series of half or whole steps, e.g. C wwhwwwh")
            else:
                print("invalid input")




    elif int(s) == 2:
        print("enter a series of notes.  e for menu")
        notes = sys.stdin.readline().split()
        #specify root note, selection statement if all in AND root is [1] of scale
        output = ["".join(scale) for scale in scales if all(elem in scale for elem in notes)]
        #less efficient going through the for loop twice but looks much more readable, fix
        for line in output:
            print(line)
    
    elif int(s) == 3:
        print("".join(random.choice(scales)))




    else:
        print("invalid input, try again" + '\n')