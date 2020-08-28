# Initialization
import webbrowser
import sys
from dbfirg import *
print("˜*•. ˜”*°•.˜”* °••°*”˜.•°*”˜˜*•. ˜”*°•.˜”")
print("FICHIER INTL. DES RENSEIGNEMENTS GÉNÉRAUX")
print("    International League of Diplomacy    ")
print("        Restricted Access, 2.1.0         ")
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
                print("SEARCH : Research somebody in the international database.\nLEGEND : Get the legend of citizenships files.\nSTATS : Get the citizenships statistics.\nDATABASES : Get the list of other official databases.\nCLASSIFIED : Access to classified informations with a special habilitation.\nVERSION : See the current version and update notes.\nWEBSITE : Get League's official link.")
                continue
            if cmd == "SEARCH":
                print("Start searching a matching input like the example or with a identity international number.\nEx. DUPONT, Auguste or TMSCDUAU0001.")
                continue
            if cmd == "LEGEND":
                print("(1) INTERNATIONAL IDENTIFICATION NUMBER\n(2) FIRST NAME, NAME\n(3) NATIONALITIES, CLASS\n\n(4) BIRTH YEAR, BIRTH LOCATION -\n(5) GENDER, TALL\n(6) DOMICILIATION\n\n(7) CRIMINAL RECORDS\n(8) SPECIAL NOTES\n\n(*) COULD BE FOUND\n(7) DIPLOMATIC IMMUNITY, SECRET DEFENSE HABILITATION REQUIERED IN SPECIAL INTERNATIONAL FILE ACCESS")
                continue
            if cmd == "STATS":
                print("TERREMYSTIAN IDENTITIES (12)\nCitizens (6), Diplomates (6)\nTERCIAN IDENTITIES (2)\nCitizens (0), Diplomates (2)\nAQUILEIAN IDENTITES (2)\nCitizens (0), Diplomates (2)\nELEFSERIAN IDENTITIES (0)\nCitizens (0), Diplomates (0)\nEDRAISIAN IDENTITIES (1)\nCitizens (0), Diplomates (1)")
                continue
            if cmd == "VERSION":
                print("Fichier International des Renseignements Généraux [version 2.1.0]\n(c) August 2020 Polemarch Corporation. All rights reserved.\nUpdate notes : Actualization and finalization of file's and databases's development.")
                continue
            if cmd == "CLASSIFIED":
                print("You're trying to access to classified informations : a special SECRET DEFENSE PASSWORD will be required.\nWARNING. This will break the current program.")
                key = input()
                SPECIALKEY = "".join([chr(int(binary, 2)) for binary in SPECIALKEY.split(" ")])
                if key == SPECIALKEY:
                    DECRYPTED = "".join([chr(int(binary, 2)) for binary in CLASSIFIED.split(" ")])
                    print(DECRYPTED)
                    continue
                elif key != SPECIALKEY:
                    sys.exit()
            if cmd == "WEBSITE":
                print("International League of Diplomacy's website is currently loading.\nRedirection...")
                webbrowser.open('https://diplomacyleague.wordpress.com')
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
            if cmd == "DRAGNEEL, Natsu":
                DECRYPTED = "".join([chr(int(binary, 2)) for binary in TMSDDRNA0002.split(" ")])
                print(DECRYPTED)
                continue
            if cmd == "TMSDDRNA0002":
                DECRYPTED = "".join([chr(int(binary, 2)) for binary in TMSDDRNA0002.split(" ")])
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
            if cmd == "ELHIJEI, Striff":
                DECRYPTED = "".join([chr(int(binary, 2)) for binary in TMSCELST0004.split(" ")])
                print(DECRYPTED)
                continue
            if cmd == "TMSCELST0004":
                DECRYPTED = "".join([chr(int(binary, 2)) for binary in TMSCELST0004.split(" ")])
                print(DECRYPTED)
                continue
            if cmd == "BANGER, Tim":
                DECRYPTED = "".join([chr(int(binary, 2)) for binary in TMSCBATI0005.split(" ")])
                print(DECRYPTED)
                continue
            if cmd == "TMSCBATI0005":
                DECRYPTED = "".join([chr(int(binary, 2)) for binary in TMSCBATI0005.split(" ")])
                print(DECRYPTED)
                continue
            if cmd == "OLYMPUS, Alexios":
                DECRYPTED = "".join([chr(int(binary, 2)) for binary in TMSCOLAL0006.split(" ")])
                print(DECRYPTED)
                continue
            if cmd == "TMSCOLAL0006":
                DECRYPTED = "".join([chr(int(binary, 2)) for binary in TMSCOLAL0006.split(" ")])
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
        # Edraisian Database Import
            if cmd == "LAZIC, Erwan":
                DECRYPTED = "".join([chr(int(binary, 2)) for binary in EDRDLAER0001.split(" ")])
                print(DECRYPTED)
                continue
            if cmd == "EDRDLAER0001":
                DECRYPTED = "".join([chr(int(binary, 2)) for binary in EDRDLAER0001.split(" ")])
                print(DECRYPTED)
                continue
        # Error 404
            else:
                print("No data or command found.")
                continue
    # Final Break
    elif key != KEY:
        sys.exit()