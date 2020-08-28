# Initialization
import webbrowser
import sys
from dbftir import *
print("˜*•. ˜”*°•.˜”* °••°*”˜.•°*”˜˜*•. ˜”*°•.˜”")
print("  FICHIER DES INFRACTIONS RÉPERTORIÉES   ")
print("   Ministère des Affaires Intérieures    ")
print("        Restricted Access, 1.1.0         ")
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
                print("INFRATERR : Get the complete list of infractions in the 'INFRActions TERRemystiennes' database.\nINFRAMYTH : Get the complete list of infractions in the 'INFRActions MYTHologiques' database. WARNING. STATE SECRET CLASSIFIED.\nVERSION : Get the current version informations.\nWEBSITE : Go to Government website.")
                continue
            if cmd == "INFRATERR":
                DECRYPTED = "".join([chr(int(binary, 2)) for binary in INFRATERR.split(" ")])
                print(DECRYPTED)
                continue
            if cmd == "INFRAMYTH":
                print("You're trying to access to classified informations : a special STATE SECRET password will be required.\nWARNING. This will break the current program.")
                key = input()
                SPECIALKEY = "".join([chr(int(binary, 2)) for binary in SPECIALKEY.split(" ")])
                if key == SPECIALKEY:
                    DECRYPTED = "".join([chr(int(binary, 2)) for binary in INFRAMYTH.split(" ")])
                    print(DECRYPTED)
                    continue
                elif key != SPECIALKEY:
                    sys.exit()
            if cmd == "VERSION":
                print("Fichier Terremystien des Infractions Répertoriées [version 1.1.0]\n(c) August 2020 Polemarch Corporation. All rights reserved.\nUpdate notes : Actualization and finalization of file's and databases's development.")
                continue
            if cmd == "WEBSITE":
                print("Terremystian Government's website is currently loading.\nRedirection...")
                webbrowser.open('https://terremystique.wordpress.com')
                continue
            if cmd == "EXIT":
                break
        # Error 404
            else:
                print("No data or command found.")
                continue
    # Final Break
    elif key != KEY:
        sys.exit()