# Initialization
import webbrowser
import sys
from db import *
print("˜*•. ˜”*°•.˜”* °••°*”˜.•°*”˜˜*•. ˜”*°•.˜”")
print("     CITIZENSHIPS INTERNATIONAL FILE     ")
print("    International League of Diplomacy    ")
print("      Low Habilitation Mode, 1.1.0       ")
print("˜*•. ˜”*°•.˜”* °••°*”˜.•°*”˜˜*•. ˜”*°•.˜”")
print("\n\n(c) August 2020 Polemarch Corporation. All rights reserved.\n\nPlease enter START to get starting.\n\n")
init = input()

# Security Control
if init == "START":
    print("Program initialization...")
    print("")
    print("Password requiered.\nWARNING. A false password break the program.")
    key = input()
    KEY = "".join([chr(int(binary, 2)) for binary in KEY.split(" ")])
    if key == KEY:
        print("\nInitialization completed.\nGet help with HELP command or start searching. Close the program with EXIT.\n\n")
    # Main Commands
        while True:
            cmd = input()
            if cmd == "HELP":
                print("SEARCH : Research somebody in the international database.\nLEGEND : Get the legend of citizenships files.\nSTATS : Get the citizenships statistics.\nDATABASES : Get the list of other official databases.\nVERSION : See the current version and update notes.\nWEBSITE : Get League's official link.")
                continue
            if cmd == "SEARCH":
                print("Start searching a matching input like the example or with a identity international number.\nEx. DUPONT, Auguste or TMSCDUAU0001.")
                continue
            if cmd == "LEGEND":
                print("(1) INTERNATIONAL IDENTIFICATION NUMBER\n(2) FIRST NAME, NAME\n(3) NATIONALITIES, CLASS\n\n(4) BIRTH YEAR, BIRTH LOCATION -\n(5) GENDER, TALL\n(6) DOMICILIATION\n\n(7) CRIMINAL RECORDS\n(8) SPECIAL NOTES\n\n(*) COULD BE FOUND\n(7) DIPLOMATIC IMMUNITY, SECRET DEFENSE HABILITATION REQUIERED IN SPECIAL INTERNATIONAL FILE ACCESS")
                continue
            if cmd == "STATS":
                print("TERREMYSTIAN IDENTITIES (6)\nCitizens (2), Diplomates (4)\nTERCIAN IDENTITIES (2)\nCitizens (0), Diplomates (2)\nAQUILEIAN IDENTITES (2)\nCitizens (0), Diplomates (2)\nELEFSERIAN IDENTITIES (0)\nCitizens (0), Diplomates (0)")
                continue
            if cmd == "DATABASES":
                print("No databases found. Other databases could be in development.")
                continue
            if cmd == "VERSION":
                print("Citizenships International File Project [version 1.1.0]\n(c) August 2020 Polemarch Corporation. All rights reserved.\nUpdate notes : Creation of the current program. Functionnalities will arrive.")
                continue
            if cmd == "WEBSITE":
                print("International League of Diplomacy's website is currently in development.\nRedirection...")
                webbrowser.open('https://terremystique.wordpress.com')
                continue
            if cmd == "EXIT":
                break
        # Terremystian Database Import
            if cmd == "MACHADO, Quentin":
                DECRYPTED = "".join([chr(int(binary, 2)) for binary in TMSDMAQU0001.split(" ")])
                print(DECRYPTED)
                continue
            if cmd == "TMSDMAQU0001":
                DECRYPTED = "".join([chr(int(binary, 2)) for binary in TMSDMAQU0001.split(" ")])
                print(DECRYPTED)
                continue
            if cmd == "KARENA, Emma":
                DECRYPTED = "".join([chr(int(binary, 2)) for binary in TMSCKAEM0001.split(" ")])
                print(DECRYPTED)
                continue
            if cmd == "TMSCKAEM0001":
                DECRYPTED = "".join([chr(int(binary, 2)) for binary in TMSCKAEM0001.split(" ")])
                print(DECRYPTED)
                continue
            if cmd == "NATSUYOKI, Bernard":
                DECRYPTED = "".join([chr(int(binary, 2)) for binary in TMSCNABE0002.split(" ")])
                print(DECRYPTED)
                continue
            if cmd == "TMSCNABE0002":
                DECRYPTED = "".join([chr(int(binary, 2)) for binary in TMSCNABE0002.split(" ")])
                print(DECRYPTED)
                continue
            if cmd == "HAMIBOUF, Aziz":
                DECRYPTED = "".join([chr(int(binary, 2)) for binary in TMSCHAAZ0003.split(" ")])
                print(DECRYPTED)
                continue
            if cmd == "TMSCHAAZ0003":
                DECRYPTED = "".join([chr(int(binary, 2)) for binary in TMSCHAAZ0003.split(" ")])
                print(DECRYPTED)
                continue
        # Tercian Database Import
            if cmd == "JORVASKI, Michel":
                DECRYPTED = "".join([chr(int(binary, 2)) for binary in RFTDJOMI0001.split(" ")])
                print(DECRYPTED)
                continue
            if cmd == "RFTDJOMI0001":
                DECRYPTED = "".join([chr(int(binary, 2)) for binary in RFTDJOMI0001.split(" ")])
                print(DECRYPTED)
                continue
            if cmd == "D'ATHINAIOS, Apollinarios":
                DECRYPTED = "".join([chr(int(binary, 2)) for binary in RFTDATAP0002.split(" ")])
                print(DECRYPTED)
                continue
            if cmd == "RFTDATAP0002":
                DECRYPTED = "".join([chr(int(binary, 2)) for binary in RFTDATAP0002.split(" ")])
                print(DECRYPTED)
                continue
        # Aquileian Database Import
            if cmd == "AHO, Timothée":
                DECRYPTED = "".join([chr(int(binary, 2)) for binary in AQMDAHTI0001.split(" ")])
                print(DECRYPTED)
                continue
            if cmd == "AQMDAHTI0001":
                DECRYPTED = "".join([chr(int(binary, 2)) for binary in AQMDAHTI0001.split(" ")])
                print(DECRYPTED)
                continue
            if cmd == "ROBINSON, Nicholas":
                DECRYPTED = "".join([chr(int(binary, 2)) for binary in AQMDRONI0002.split(" ")])
                print(DECRYPTED)
                continue
            if cmd == "AQMDRONI0002":
                DECRYPTED = "".join([chr(int(binary, 2)) for binary in AQMDRONI0002.split(" ")])
                print(DECRYPTED)
                continue
        # Error 404
            else:
                print("No data or command found.")
                continue
    # Final Break
    elif key != KEY:
        sys.exit()