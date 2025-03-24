import os
from sys import stdout
from colorama import Fore

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def banners():
    clear_terminal()
    stdout.write("                                                                                         \n")
    stdout.write(""+Fore.LIGHTRED_EX +"██╗   ██╗██████╗ ██████╗ ████████╗ ██████╗ \n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║   ██║██╔══██╗╚════██╗╚══██╔══╝██╔════╝ \n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║   ██║██████╔╝ █████╔╝   ██║   ██║  ███╗\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║   ██║██╔═══╝ ██╔═══╝    ██║   ██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"╚██████╔╝██║     ███████╗   ██║  ╚██████╔ ╝\n")
    stdout.write(""+Fore.LIGHTRED_EX +" ╚═════╝ ╚═╝     ╚══════╝   ╚═╝    ╚═════╝ \n")
    stdout.write(""+Fore.YELLOW +"═════════════╦═════════════════════════════════╦══════════════════════════════\n")
    stdout.write(""+Fore.YELLOW   +"╔════════════╩═════════════════════════════════╩═════════════════════════════╗\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"AUTHOR             "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   PARI MALAM                                    "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"╔════════════════════════════════════════════════════════════════════════════╝\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"GITHUB             "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   GITHUB.COM/THATNOTEASY                        "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"╚════════════════════════════════════════════════════════════════════════════╝\n") 
    print(f"{Fore.YELLOW}[UP2TG] - {Fore.GREEN}Telegram Larger File Uploader - {Fore.RED}[V1.0] \n{Fore.RESET}")