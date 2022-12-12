import os, secrets
from colorama import Fore, Style

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_console()

length = int(input("enter the length of the password (1-999): "))
password = secrets.token_urlsafe(length)

clear_console()

print(f'''- generated password: {Fore.GREEN}{password}{Style.RESET_ALL}
- num of random bytes: {Fore.GREEN}{length}{Style.RESET_ALL}''')