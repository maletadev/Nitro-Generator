import random
import string
from colorama import Fore, Style, init
import os

init()

def generate_link():
    return "https://discord.gift/" + ''.join(random.choices(string.ascii_letters + string.digits, k=16))

def show_title():
    title = """\n\n███╗   ██╗██╗████████╗██████╗  ██████╗      ██████╗ ███████╗███╗   ██╗
████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗    ██╔════╝ ██╔════╝████╗  ██║
██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║    ██║  ███╗█████╗  ██╔██╗ ██║
██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║    ██║   ██║██╔══╝  ██║╚██╗██║
██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝    ╚██████╔╝███████╗██║ ╚████║
╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝"""
    
    width = os.get_terminal_size().columns
    
    for line in title.splitlines():
        print(Fore.MAGENTA + line.center(width) + Style.RESET_ALL)
    
    print()
    
    text = "developed by"
    name = "@maletadev"
    full = text + name
    centered = full.center(width)
    
    start = centered.find(name)
    end = start + len(name)
    
    print(
        Fore.MAGENTA + centered[:start] +
        Fore.WHITE + centered[start:end] +
        Fore.MAGENTA + centered[end:] +
        Style.RESET_ALL
    )

def show_links(links):
    print(Fore.MAGENTA + f"\nSuccessfully generated {len(links)} gift links ↓" + Style.RESET_ALL)
    print(Fore.MAGENTA + "-"*42 + Style.RESET_ALL)
    for l in links:
        print(Fore.GREEN + "[+] " + l + Style.RESET_ALL)
    print(Fore.MAGENTA + "-"*42 + Style.RESET_ALL)

def save_links(links):
    fname = input(Fore.MAGENTA + "Filename (without extension): " + Style.RESET_ALL).strip() + ".txt"
    with open(fname, "w") as f:
        for l in links:
            f.write(l + "\n")
    print(Fore.MAGENTA + f"Links saved to {fname}" + Style.RESET_ALL)

def main():
    show_title()
    
    while True:
        try:
            count = int(input(Fore.MAGENTA + "\nHow many nitros to generate: " + Style.RESET_ALL))
            links = [generate_link() for _ in range(count)]
            show_links(links)
            
            save = input(Fore.MAGENTA + "Save links to file? (yes/no): " + Style.RESET_ALL).lower().strip()
            if save == "yes":
                save_links(links)
            
            nxt = input(Fore.MAGENTA + "\nPress Enter to generate more or type 'exit' to quit: " + Style.RESET_ALL)
            if nxt.lower() == "exit":
                break
                
        except ValueError:
            print(Fore.MAGENTA + "Please enter a number!" + Style.RESET_ALL)
        except KeyboardInterrupt:
            print(Fore.MAGENTA + "\nGoodbye!" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    main()
