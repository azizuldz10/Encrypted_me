from colorama import init, Fore, Style
import getpass
from ..core.encryptor import AdvancedFileEncryptor
from ..config import settings

init()

def display_menu():
    print(f"\n{Fore.CYAN}🔐 Advanced File Encryption Tool{Style.RESET_ALL}")
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. Encrypt Folder")
    print("4. Decrypt Folder")
    print("5. Show Statistics")
    print("6. Compression Settings")
    print("7. Exit")

def get_compression_preferences():
    print(f"\n{Fore.YELLOW}Available compression methods:{Style.RESET_ALL}")
    for i, method in enumerate(settings.COMPRESSION_METHODS, 1):
        print(f"{i}. {method}")
    
    method_choice = input("Choose compression method (1-3): ")
    compress = input("Enable compression? (y/n): ").lower() == 'y'
    
    return {
        'compress': compress,
        'method': settings.COMPRESSION_METHODS[int(method_choice)-1] if compress else None
    } 