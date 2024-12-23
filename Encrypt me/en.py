from cryptography.fernet import Fernet
from pathlib import Path
import os
import base64
import hashlib
import getpass
import logging
import json
import time
from tqdm import tqdm
from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored output
init()

class AdvancedFileEncryptor:
    def __init__(self):
        self.config_file = "encryption_config.json"
        self.setup_logging()
        self.load_config()
        
    def setup_logging(self):
        logging.basicConfig(
            filename='encryption.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def load_config(self):
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    self.config = json.load(f)
            else:
                self.config = {
                    'encrypted_files': [],
                    'encryption_count': 0,
                    'last_encryption': None
                }
        except Exception as e:
            logging.error(f"Error loading config: {str(e)}")
            self.config = {
                'encrypted_files': [],
                'encryption_count': 0,
                'last_encryption': None
            }

    def save_config(self):
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=4)
        except Exception as e:
            logging.error(f"Error saving config: {str(e)}")

    def generate_key(self, password):
        salt = b'complex_salt_value_here'
        kdf = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        return base64.urlsafe_b64encode(kdf)

    def encrypt_file(self, file_path, password):
        try:
            key = self.generate_key(password)
            f = Fernet(key)
            
            print(f"{Fore.YELLOW}⚡ Encrypting: {file_path}{Style.RESET_ALL}")
            
            # Read file content
            with open(file_path, 'rb') as file:
                file_data = file.read()
                
            # Encrypt data with progress bar
            encrypted_data = f.encrypt(file_data)
            
            # Save encrypted file
            encrypted_path = str(file_path) + '.encrypted'
            with open(encrypted_path, 'wb') as file:
                file.write(encrypted_data)
                
            # Update config
            self.config['encrypted_files'].append({
                'original_path': str(file_path),
                'encrypted_path': encrypted_path,
                'timestamp': time.time()
            })
            self.config['encryption_count'] += 1
            self.config['last_encryption'] = time.strftime('%Y-%m-%d %H:%M:%S')
            self.save_config()
            
            print(f"{Fore.GREEN}✅ Successfully encrypted: {file_path}{Style.RESET_ALL}")
            logging.info(f"File encrypted: {file_path}")
            
            return True
            
        except Exception as e:
            print(f"{Fore.RED}❌ Error encrypting {file_path}: {str(e)}{Style.RESET_ALL}")
            logging.error(f"Encryption error for {file_path}: {str(e)}")
            return False

    def decrypt_file(self, encrypted_file, password):
        try:
            key = self.generate_key(password)
            f = Fernet(key)
            
            print(f"{Fore.YELLOW}🔓 Decrypting: {encrypted_file}{Style.RESET_ALL}")
            
            # Read encrypted data
            with open(encrypted_file, 'rb') as file:
                encrypted_data = file.read()
                
            # Decrypt data
            decrypted_data = f.decrypt(encrypted_data)
            
            # Save decrypted file
            decrypted_path = str(encrypted_file).replace('.encrypted', '')
            with open(decrypted_path, 'wb') as file:
                file.write(decrypted_data)
                
            print(f"{Fore.GREEN}✅ Successfully decrypted: {encrypted_file}{Style.RESET_ALL}")
            logging.info(f"File decrypted: {encrypted_file}")
            
            return True
            
        except Exception as e:
            print(f"{Fore.RED}❌ Error decrypting {encrypted_file}: {str(e)}{Style.RESET_ALL}")
            logging.error(f"Decryption error for {encrypted_file}: {str(e)}")
            return False

    def encrypt_folder(self, folder_path, password):
        folder = Path(folder_path)
        if not folder.exists():
            print(f"{Fore.RED}❌ Folder not found: {folder_path}{Style.RESET_ALL}")
            return False
            
        success = True
        files = list(folder.rglob('*'))
        
        with tqdm(total=len(files), desc="Encrypting folder") as pbar:
            for file in files:
                if file.is_file() and not str(file).endswith('.encrypted'):
                    if not self.encrypt_file(str(file), password):
                        success = False
                pbar.update(1)
                
        return success

    def decrypt_folder(self, folder_path, password):
        folder = Path(folder_path)
        if not folder.exists():
            print(f"{Fore.RED}❌ Folder not found: {folder_path}{Style.RESET_ALL}")
            return False
            
        success = True
        encrypted_files = list(folder.rglob('*.encrypted'))
        
        with tqdm(total=len(encrypted_files), desc="Decrypting folder") as pbar:
            for file in encrypted_files:
                if not self.decrypt_file(str(file), password):
                    success = False
                pbar.update(1)
                
        return success

    def show_statistics(self):
        print(f"\n{Fore.CYAN}📊 Encryption Statistics:{Style.RESET_ALL}")
        print(f"Total files encrypted: {self.config['encryption_count']}")
        print(f"Last encryption: {self.config['last_encryption']}")
        print(f"Number of encrypted files tracked: {len(self.config['encrypted_files'])}\n")

def main():
    encryptor = AdvancedFileEncryptor()
    
    while True:
        print(f"\n{Fore.CYAN}🔐 Advanced File Encryption Tool{Style.RESET_ALL}")
        print("1. Encrypt File")
        print("2. Decrypt File")
        print("3. Encrypt Folder")
        print("4. Decrypt Folder")
        print("5. Show Statistics")
        print("6. Exit")
        
        choice = input(f"\n{Fore.YELLOW}Choose an option (1-6): {Style.RESET_ALL}")
        
        if choice == '6':
            break
            
        if choice == '5':
            encryptor.show_statistics()
            continue
            
        path = input(f"{Fore.YELLOW}Enter file/folder path: {Style.RESET_ALL}")
        password = getpass.getpass(f"{Fore.YELLOW}Enter encryption password: {Style.RESET_ALL}")
        
        if choice == '1':
            encryptor.encrypt_file(path, password)
        elif choice == '2':
            encryptor.decrypt_file(path, password)
        elif choice == '3':
            encryptor.encrypt_folder(path, password)
        elif choice == '4':
            encryptor.decrypt_folder(path, password)

if __name__ == "__main__":
    main()