import random
import string
from colorama import Fore, Style, init
import os

init()

def generate_discord_gift_link():
    base_url = "https://discord.gift/"
    random_code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return base_url + random_code

def display_title():
    """Display the Title and Developer Info"""
    title = """\n\n███╗   ██╗██╗████████╗██████╗  ██████╗      ██████╗ ███████╗███╗   ██╗
████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗    ██╔════╝ ██╔════╝████╗  ██║
██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║    ██║  ███╗█████╗  ██╔██╗ ██║
██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║    ██║   ██║██╔══╝  ██║╚██╗██║
██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝    ╚██████╔╝███████╗██║ ╚████║
╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝"""
    
    width = os.get_terminal_size().columns
    
    title_lines = title.splitlines()
    for line in title_lines:
        centered_title = line.center(width)
        print(Fore.RED + centered_title + Style.RESET_ALL)
    
    print()
    developer_text = "developed by @85rx"
    centered_developer_text = developer_text.center(width)
    print(Fore.RED + centered_developer_text + Style.RESET_ALL)

def display_generated_links(links):
    total_generated_links = len(links)  
    print(Fore.RED + f" Successfully generated {total_generated_links} gift links ↓" + Style.RESET_ALL)
    print(Fore.RED + "------------------------------------------" + Style.RESET_ALL)
    for link in links:
        print(f"{Fore.GREEN}[+] {link}{Style.RESET_ALL}")
    print(Fore.RED + "------------------------------------------" + Style.RESET_ALL)

def save_links_to_file(links):
    filename = input(f"{Fore.RED}Enter the filename (without extension): {Style.RESET_ALL}").strip() + ".txt"
    with open(filename, "w") as file:
        for link in links:
            file.write(link + "\n")
    print(f"{Fore.RED}Links saved to {filename}{Style.RESET_ALL}")

def main():
    display_title()

    while True:
        try:
            num_links = int(input(f"{Fore.RED}\n\n How many nitros you want to generate: {Style.RESET_ALL}"))

            generated_links = [generate_discord_gift_link() for _ in range(num_links)]
            display_generated_links(generated_links)

            save_to_file = input(f"{Fore.RED} Do you want to save the links to a text file? (yes/no): {Style.RESET_ALL}").strip().lower()

            if save_to_file == 'yes':
                save_links_to_file(generated_links)

            user_input = input(f"\n{Fore.RED} Press Enter to generate more links or type 'exit' to quit: {Style.RESET_ALL}")
            if user_input.strip().lower() == 'exit':
                break

        except ValueError:
            print(f"{Fore.RED}Please enter a valid number.{Style.RESET_ALL}")
            input(f"{Fore.RED}Press Enter to try again{Style.RESET_ALL}")

        except KeyboardInterrupt:
            print(f"\n{Fore.RED}Goodbye!{Style.RESET_ALL}")
            break

if __name__ == "__main__":
    main()
