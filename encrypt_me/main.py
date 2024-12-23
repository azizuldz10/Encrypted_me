from cli.menu import display_menu
from core.encryptor import AdvancedFileEncryptor
from core.utils import setup_logging
from colorama import Fore, Style
import getpass

def main():
    # Setup logging
    setup_logging()
    
    # Initialize encryptor
    encryptor = AdvancedFileEncryptor()
    
    while True:
        display_menu()
        choice = input(f"\n{Fore.YELLOW}Choose an option (1-7): {Style.RESET_ALL}")
        
        if choice == '7':
            print(f"{Fore.GREEN}Thank you for using our encryption tool!{Style.RESET_ALL}")
            break
            
        if choice == '5':
            encryptor.show_statistics()
            continue
            
        if choice == '6':
            compression_prefs = get_compression_preferences()
            continue
            
        path = input(f"{Fore.YELLOW}Enter file/folder path: {Style.RESET_ALL}")
        password = getpass.getpass(f"{Fore.YELLOW}Enter encryption password: {Style.RESET_ALL}")
        
        try:
            if choice == '1':
                encryptor.process_file(path, password)
            elif choice == '2':
                encryptor.decrypt_file(path, password)
            elif choice == '3':
                encryptor.encrypt_folder(path, password)
            elif choice == '4':
                encryptor.decrypt_folder(path, password)
        except Exception as e:
            print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")

if __name__ == "__main__":
    main() 